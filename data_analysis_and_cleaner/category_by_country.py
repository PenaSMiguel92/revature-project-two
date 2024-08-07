#import os
import pandas
import load_csv
from pyspark.sql import DataFrame,functions as f
from pathlib import Path

df = load_csv.load("data/clean_data.csv")

df: DataFrame = df.drop('order_id', 'customer_id', 'customer_name','product_id','product_name', 
        'payment_type', 'datetime', 'city', 'ecommerce_website_name',  
        'payment_txn_id','payment_txn_success')

df = df.withColumn("total_sales",f.round(f.col("qty") * f.col("price"),2))

df = df.groupBy("product_category", "country").agg(f.round(f.sum("qty"),0).cast("integer").alias("unit_sold"),
                                                   f.round(f.sum("total_sales"),2).alias("total_sales"))

df = df.orderBy(["product_category","country"])

# For python
path = Path(__file__).parent / "data/oluwatobi/category_by_country.csv"
df.toPandas().to_csv(str(path), index=False)

"""For jupyter
path = os.path.abspath('') + "/category_by_country"
df.write.csv('file://'+str(path), header=True) """