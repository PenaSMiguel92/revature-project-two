import load_csv
from pyspark import SparkContext, SparkConf
import sparkContext

sc = sparkContext.sc

rdd_list = load_csv.load() 

print(rdd_list.take(5))