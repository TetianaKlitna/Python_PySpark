from pyspark.sql import (
    SparkSession,
    functions as F,
)
from dataset_paths import orders_data_path

spark = (
    SparkSession
    .builder
    .appName('cleaning_orders_dataset_with_pyspark')
    .getOrCreate()
)

orders_data = spark.read.parquet(orders_data_path)
orders_data.toPandas().head()

orders_data_clean = (
    orders_data.filter(~orders_data.product.like("%TV%"))
)

orders_data_clean = (orders_data_clean
    .withColumn("product", F.lower(orders_data.product))
    .withColumn("hour", F.hour(orders_data.order_date))
)

orders_data_clean = (
    orders_data_clean
    .filter(~((0 < orders_data_clean.hour) & (orders_data_clean.hour <= 5)))
)

orders_data_clean = (
    orders_data_clean
    .withColumn("order_date", orders_data_clean.order_date.cast("date"))
    .withColumn("category", F.lower(orders_data_clean.category))
)

orders_data_clean = (
    orders_data_clean.withColumn("time_of_day",
    F.when((5 < orders_data_clean.hour) & (orders_data_clean.hour <= 12), 'morning')
     .when((12 < orders_data_clean.hour) & (orders_data_clean.hour <= 18), 'afternoon')
     .when(((18 < orders_data_clean.hour) & (orders_data_clean.hour <= 23)) | (orders_data_clean.hour == 0), 'evening')
     .otherwise('unknown'))
    .withColumn("purchase_state",
    F.regexp_extract(orders_data_clean.purchase_address, r",\s([A-Za-z]{2})\s", 1))
)

orders_data_clean = orders_data_clean.select(
     [col for col in orders_data_clean.columns if col != "hour"]
)
# This will save the file as a single Parquet file in the specified path. 
# However, coalescing into one partition might affect performance for large datasets
orders_data_clean.coalesce(1).write.mode("overwrite").parquet("Datasets/orders_data_clean.parquet")