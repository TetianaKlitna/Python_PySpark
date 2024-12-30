import pandas as pd
import numpy as np

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from dataset_paths import flights_path

sc = SparkContext('local')
print(sc.version)

spark = SparkSession.builder.getOrCreate()

# Print the tables in the catalog
print(spark.catalog.listTables())

# Read in the airports data
flights = spark.read.csv(flights_path, header=True)

# Show the data
flights.show(10)

# Print the tables in the catalog
print(spark.catalog.listTables())

# adding data into spark view for sql querying
flights.createOrReplaceTempView('flights')

# print the tables in catalog
print(spark.catalog.listTables())

# Get the first 10 rows of flights
query = "FROM flights SELECT * LIMIT 10"
flights10 = spark.sql(query)
flights10.show(truncate=False)

query = "SELECT origin_airport, destination_airport, COUNT(*) AS n FROM flights GROUP BY origin_airport, destination_airport"
flight_counts = spark.sql(query)
# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()
print(pd_counts.head())

pd_temp = pd.DataFrame(np.random.random(10))
# Convert Pandas DataFrame to PySpark DataFrame
spark_temp = spark.createDataFrame(pd_temp)
print(spark.catalog.listTables())
spark_temp.createOrReplaceTempView('temp')
print(spark.catalog.listTables())
