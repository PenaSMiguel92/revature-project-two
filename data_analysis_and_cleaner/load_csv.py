from pathlib import Path
from pyspark import SparkContext, SparkConf
import sparkContext
def load(path: str):
    #sc = sparkContext.sc
    spark = sparkContext.spark
    #used in linux distro
    path = Path(__file__).parent / path
    return spark.read.format("csv").option("header", "true").load('file://'+str(path.absolute())) 

def getContext():
    """
        Use this to get the current spark context
    """
    return sparkContext.spark