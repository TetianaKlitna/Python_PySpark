from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, round, col
from dataset_paths import flights_path

spark = SparkSession.builder.getOrCreate()

flights = spark.read.csv(flights_path, header=True)
# Cast columns to appropriate data types
flights = flights.withColumn("distance", col("distance").cast("integer")) \
                 .withColumn("air_time", col("air_time").cast("integer"))
flights.createOrReplaceTempView('flights')
# Add columns duration_hrs, country
flights = flights.withColumn("duration_hr", round(flights.air_time/60, 2)) \
                 .withColumn("country", lit("USA"))
flights.show(10)

# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

long_flights1.show(10)
long_flights2.show(10)

selected1 = flights.select("tailnum", "origin", "dest")
selected1.show(10)

temp = flights.select(flights.origin, flights.dest, flights.carrier)
filterA = flights.origin == 'SEA'
filterB = flights.dest == 'PDX'
selected2 = temp.filter(filterA) \
                .filter(filterB)
selected2.show(10)

avg_speed = round((flights.distance/(flights.air_time/60)),
                  2).alias("avg_speed")
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
speed1.show(10)

speed2 = flights.selectExpr(
    "origin", "dest", "tailnum", "round(distance/(air_time/60), 2) as avg_speed")
speed2.show(10)

column_info = flights.dtypes
print(column_info)

# Find the shortest flight from PDX in terms of dis
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()
# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()
# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(
    flights.origin == "SEA").groupBy().avg("air_time").show()
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60) \
       .groupBy() \
       .sum("duration_hrs") \
       .show()
