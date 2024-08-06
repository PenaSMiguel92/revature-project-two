#import findspark
#findspark.init()

from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder \
    .appName("JupyterPySpark") \
    .getOrCreate()

if __name__ == "__main__":
    # Verify the Spark session and context
    print(spark)