from pyspark.sql import SparkSession

# Build sparkSession object
spark = SparkSession.builder \
    .master("local") \
    .appName("df_intro") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

# file location defaults to hdfs on localhost. To use local fs, use "file://{absolute-path}"
df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load('file:///home/gabrielklein/pokemon_1.csv')

df.show(5)

df.select(["Attack", "Legendary"]) \
    .groupBy("Legendary") \
    .avg("Attack") \
    .show()

df.write.format("csv").save("file:///home/gabrielklein/pokemon_data")