from pathlib import Path
from pyspark import SparkContext, SparkConf
import sparkContext
def load():
    #sc = sparkContext.sc
    spark = sparkContext.spark
    #used in linux distro
    path = Path(__file__).parent / "data/data_team_3.csv"
    return spark.read.format("csv").option("header", "true").load('file://'+str(path.absolute())) 