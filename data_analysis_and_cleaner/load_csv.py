from pathlib import Path
from pyspark import SparkContext, SparkConf
import sparkContext
def load():
    sc = sparkContext.sc
    path = Path(__file__).parent / "data/data_team_3.csv"
    path.resolve()
    print(path.absolute().root)
    data_team_3_rdd = sc.textFile('file:///home/miguel674-rev/2009_Big_Data/revature-2/Revature_Project_2/data/data_team_3.py')
    return data_team_3_rdd.map(lambda x: x.split(','))