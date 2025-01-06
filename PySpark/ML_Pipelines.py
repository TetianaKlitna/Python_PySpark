from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

import numpy as np
from dataset_paths import planes_path, flights_path

spark = SparkSession.builder.getOrCreate()
flights = spark.read.csv(flights_path, header=True)
planes = spark.read.csv(planes_path, header=True)
planes = planes.withColumnRenamed("year", "plane_year")
model_data = flights.join(planes, on="tailnum", how="leftouter")
# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer")) \
                       .withColumn("air_time", model_data.air_time.cast("integer")) \
                       .withColumn("month", model_data.month.cast("integer")) \
                       .withColumn("plane_year", model_data.plane_year.cast("integer"))
# Create the column plane_age
model_data = model_data.withColumn(
    "plane_age", model_data.year - model_data.plane_year)
# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))
# Remove missing data
model_data = model_data.filter("arr_delay IS NOT NULL AND dep_delay IS NOT NULL AND air_time IS NOT NULL AND plane_year IS NOT NULL")

carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")
dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")

flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])
piped_data = flights_pipe.fit(model_data).transform(model_data)
# Split the data into training 60% and  40% sets
training, test = piped_data.randomSplit([0.6, 0.4])

lr = LogisticRegression()
evaluator = BinaryClassificationEvaluator(metricName="areaUnderROC")

grid = ParamGridBuilder()
grid = grid.addGrid(lr.regParam, np.arange(0, 0.1, 0.01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])
grid = grid.build()

cv = CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator)
# Fit cross validation models
models = cv.fit(training)
# Extract the best model
best_lr = models.bestModel

test_result = best_lr.transform(test)
print(evaluator.evaluate(test_result))