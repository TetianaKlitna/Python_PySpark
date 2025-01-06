# DataFrames designed for processing both structured (e. g. relation database)
# and semi-structured data (e. g. JSON)

# SparkSession provides a single point of entry to interact with Spark DataFrames

# DataFrames support both SQL queries (select * from table) or expression methods (df.select())
# Creating DataFrames: 
# from existing RDDs using SparkSession's createDataFrame method
# from various data sources (csv, json, txt) using SparkSession's read method

# schema controls the data and helps DataFrames to optimize queries
# basic DataFrame transformations: select(), filter(), groupby(), orderby(), dropDuplicates(), withColumnRenamed()
# printSchema()

# Data visualization: 
# Pyspark_dist_explore library hist(), distplot() pandas_histogram()
# HandySpark package visualization

# When you have large volume of data .toPandas() isn't recomended! Pandas DataFrame is In-memory
# operations in PySpark are lazy evaluation

#Pandas DataFrame is mutable; PySpark DataDrame is immutable

from pyspark import SparkContext
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
from dataset_paths import people_path, fifa2018_path

sc = SparkContext(appName="DirectSparkContext")
rdd = sc.parallelize([ ("Tania", 35), ("Vova", 40), ("Sveta", 38)])
print("The type of RDD is", type(rdd))

# Create a PySpark DataFrame
spark = SparkSession.builder.getOrCreate()
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])
print("The type of names_df is", type(names_df))

# header = True - read scema from header
# inferSchema = True - try define data types
people_df = spark.read.csv(people_path, header=True, inferSchema=True)
people_df = people_df.select("person_id", "name", "sex", "date of birth")
print("The type of people_df is", type(people_df))

people_df.show(10)
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))
print("There are {} columns in the people_df DataFrame and their names are {}".format(len(people_df.columns), people_df.columns))

people_df_sub = people_df.select('name', 'sex', 'date of birth')
people_df_sub.show(10)
people_df_sub_nodup = people_df_sub.dropDuplicates()
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(people_df_sub.count(), people_df_sub_nodup.count()))

# Filter people_df to select females 
people_df_female = people_df.filter(people_df.sex == "female")
# Filter people_df to select males
people_df_male = people_df.filter(people_df.sex == "male")
print("There are {} rows in the people_df_female DataFrame and {} rows in the people_df_male DataFrame".format(people_df_female.count(), people_df_male.count()))

# Create a temporary table "people"
people_df.createOrReplaceTempView("people")

query = '''SELECT name FROM people'''
people_df_names = spark.sql(query)
people_df_names.show(10)

# Filter the people table to select female sex 
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')
# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * from people WHERE sex=="male"')
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))

print("The column names of names_df are", names_df.columns)  
df_pandas = names_df.toPandas()
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()

fifa_df = spark.read.csv(fifa2018_path, header=True, inferSchema=True)
fifa_df.printSchema()
fifa_df.show(10)
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))
fifa_df.createOrReplaceTempView('fifa_df_table')
query = '''SELECT Age FROM fifa_df_table WHERE Nationality == "Germany"'''
fifa_df_germany_age = spark.sql(query)
fifa_df_germany_age.describe().show()

fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()