from pyspark import SparkContext, SparkConf
import sparkContext
def load():
    sc = sparkContext.sc

    #Change for your file need
    data_team_3_rdd = sc.textFile("file:///home/badewa45/Revature_Project_2/data_analysis_and_cleaner/data/data_team_3.csv")

    return data_team_3_rdd.map(lambda x: x.split(','))