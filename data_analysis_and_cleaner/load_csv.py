from pathlib import Path
import sparkContext
def load():
    sc = sparkContext.sc
    path = Path(__file__).parent / "../data/data_team_3.csv"
    data_team_3_rdd = sc.textFile(path.as_uri)
    return data_team_3_rdd.map(lambda x: x.split(','))