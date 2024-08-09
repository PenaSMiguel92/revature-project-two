import load_csv
import pandas
from pathlib import Path
from pyspark.sql.functions import col, countDistinct
from pyspark.sql import Row
# Load Data as a DataFrame
df = load_csv.load("data/data_team_3.csv")


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

# Drop rows where 'country' is 'country'
df = df.filter(col("country") != 'country')



def shorten_names(row):
    row_dict: dict = row.asDict()
    cur_name = row_dict['product_name']
    if len(cur_name) > 30:
        word_list = cur_name.split(' ')
        name = ' '.join([word.title() for word in word_list if word.isalpha()][:3])
        row_dict.update({'product_name': name[:30]})
    
    return Row(**row_dict)

df = df.rdd.map(shorten_names).toDF()

def unique_values_count(df):
    unique_counts = {}
    for column in df.columns:
        unique_count = df.select(countDistinct(column)).collect()[0][0]
        unique_counts[column] = unique_count
    return unique_counts


path = Path(__file__).parent / "data/clean_data.csv"

# Output the Cleaned DataFrame as a CSV
df.toPandas().to_csv(str(path), index=False)

# Write DataFrame to CSV with overwrite mode
df.write.mode("overwrite").csv('file://' + str(path.absolute()), header=True)
