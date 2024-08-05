from pathlib import Path
from pyspark import SparkContext, SparkConf
import sparkContext
def load():
    sc = sparkContext.sc
    path = Path(__file__).parent / "data/data_team_3.csv"
    data_team_3_rdd = sc.textFile('File://'+str(path.absolute().as_posix))
    return data_team_3_rdd.map(lambda x: x.split(','))