# RDD - Resilient Distributed Dataset
# basic RDD transformation: map(), filter(), union(), flatMap()
# basic RDD actins: collect(), take(n), first(), count()
from pyspark import SparkContext
from dataset_paths import airports_path

sc = SparkContext(appName="DirectSparkContext")
RDD = sc.parallelize(["Spark", "is", "a", "framework",
                     "for", "Big Data processing"])
print("The type of RDD is", type(RDD))

fileRDD = sc.textFile(airports_path)
print("The file type of fileRDD is", type(fileRDD))
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())
parsed_rdd = fileRDD.map(lambda line: line.split(','))
for row in parsed_rdd.take(5):
    print(row)

fileRDD_part = sc.textFile(airports_path, minPartitions=5)
print("Number of partitions in fileRDD_part is",
      fileRDD_part.getNumPartitions())

numbRDD = sc.parallelize([1, 2, 3, 4, 5, 6])
cubedRDD = numbRDD.map(lambda x: pow(x, 3))
numbers_all = cubedRDD.collect()
for numb in numbers_all:
    print(numb)

fileRDD_filter = fileRDD.filter(lambda line: 'Airport' in line)
print("The total number of lines with the keyword Airport is", fileRDD_filter.count())
for line in fileRDD_filter.take(4):
    print(line)

# RDD key/value pairs: reduceByKey(), groupByKey(), sortByKey(), join()
Rdd = sc.parallelize([(1, 2), (3, 4), (3, 6), (4, 5)])
Rdd_Reduced = Rdd.reduceByKey(lambda x, y: x + y)
for num in Rdd_Reduced.collect(): 
  print("Key {} has {} Counts".format(num[0], num[1]))

Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)
for num in Rdd_Reduced_Sort.collect():
  print("Key {} has {} Counts".format(num[0], num[1]))

# Count the unique keys
total = Rdd.countByKey()
print("The type of total is", type(total))
for k, v in total.items(): 
  print("key", k, "has", v, "counts")

baseRDD = sc.textFile(airports_path)
# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())
print("Total number of words in splitRDD:", splitRDD.count())

stop_words = ['airport']
# Convert the words in lower case and remove stop words from the stop_words curated list
splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)
# Create a tuple of the word and 1 
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))
# Count of the number of occurences of each word
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)

# Display the first 10 words and their frequencies from the input RDD
for word in resultRDD.take(10):
	print(word)
# Swap the keys and values from the input RDD
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))
# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)
# Show the top 10 most frequent words and their frequencies from the sorted RDD
for word in resultRDD_swap_sort.take(10):
	print("{},{}". format(word[1], word[0]))