from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Example1").setMaster("local")

sc = SparkContext(conf=conf).setLogLevel("WARN")

rdd = sc.parallelize([1, 2, 3, 4, 5])

print(rdd.collect())

pokemon_rdd = sc.textFile("/home/gabrielklein/pokemon.csv")

pokemon_rdd_list = pokemon_rdd.map(lambda x: x.split(","))

print(pokemon_rdd_list.take(5))

pokemon_rdd_list.saveAsTextFile("/home/gabrielklein/pyspark_ex_out")
