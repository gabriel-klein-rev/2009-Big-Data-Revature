from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Spark_Consumer") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic1") \
    .load()

query = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

query.awaitTermination()