import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct

# Create a Spark session
spark = SparkSession.builder \
    .appName("JupyterPySpark") \
    .getOrCreate()

# Access the Spark context from the Spark session
sc = spark.sparkContext

# Verify the Spark session and context
print(spark)
print(sc)

# Have to change the path to the location of the data file
df = spark.read.format("csv").option("header", "true").load("/Users/matthewbernhardt/Desktop/data_team_3.csv")


# Filter out rows where 'payment_txn_success' is 'Y'
df = df.filter(df["payment_txn_success"] == 'Y')

#  Drop Failure Reason Column
df = df.drop("failure reason")


# Define a list of columns to check for 'CORRUPTED'
columns_to_check = df.columns
print(columns_to_check)

# Create a filter to exclude rows where any column value is 'CORRUPTED'
for column in columns_to_check[1:]:
    df = df.filter((col(column).isNotNull()) & (col(column) != "CORRUPTED"))

# Apply the filter to the DataFrame
df.count()


def unique_values_count(df):
    unique_counts = {}
    for column in df.columns:
        unique_count = df.select(countDistinct(column)).collect()[0][0]
        unique_counts[column] = unique_count
    return unique_counts

print(unique_values_count(df))

# Output the Cleaned DataFrame as a CSV
df.write.csv("cleaned_data", header=True)