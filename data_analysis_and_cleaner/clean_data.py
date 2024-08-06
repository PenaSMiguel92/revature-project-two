import load_csv
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct


# Access the Spark context from the Spark session
#sc = spark.sparkContext

# Verify the Spark session and context
#print(spark)
#print(sc)

# Have to change the path to the location of the data file
df = load_csv.load()
#spark.read.format("csv").option("header", "true").load("/Users/matthewbernhardt/Desktop/data_team_3.csv")


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


def unique_values_count(df):
    unique_counts = {}
    for column in df.columns:
        unique_count = df.select(countDistinct(column)).collect()[0][0]
        unique_counts[column] = unique_count
    return unique_counts

print(unique_values_count(df))

path = Path(__file__).parent / "test_data"

# Output the Cleaned DataFrame as a CSV
df.write.csv('file://'+str(path.absolute()), header=True)
#df.write.csv("cleaned_data", header=True)