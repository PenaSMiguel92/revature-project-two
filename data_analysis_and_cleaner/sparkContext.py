from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Cleaning_Data").setMaster("local")
sc = SparkContext(conf = conf)