#import os
import load_csv
import pandas
from pyspark.sql import DataFrame,Window,functions as f
from pathlib import Path

df = load_csv.load("data/clean_data.csv")

df: DataFrame = df.drop('order_id', 'customer_id', 'customer_name','product_id',
        'product_name','payment_type', 'datetime', 'city', 'ecommerce_website_name',  
        'payment_txn_id','payment_txn_success')

df = df.withColumn("total_sales",f.round(f.col("qty") * f.col("price"),2))

df = df.groupBy("product_category", "country")\
        .agg(f.round(f.sum("qty"),0).cast("integer")\
        .alias("unit_sold"),f.round(f.sum("total_sales"),2)\
        .alias("total_sales"))
        
df = df.orderBy(["product_category","country"])

windowSpec = Window.partitionBy("country")

county_max_total_sale_df = df.withColumn("max_total_sales", 
        f.max(f.col("total_sales"))\
        .over(windowSpec))

county_max_total_sale_df = county_max_total_sale_df\
        .filter(f.col("total_sales") == f.col("max_total_sales"))\
        .drop("max_total_sales","unit_sold")

county_max_unit_sold_df = df.withColumn("max_unit_sold", 
        f.max(f.col("unit_sold"))\
        .over(windowSpec))

county_max_unit_sold_df = county_max_unit_sold_df\
        .filter(f.col("unit_sold") == f.col("max_unit_sold"))\
        .drop("max_unit_sold","total_sales")

category_df = df.groupBy("product_category")\
        .agg(f.round(f.sum("unit_sold"),0).cast("integer").alias("unit_sold"),
        f.round(f.sum("total_sales"),2).alias("total_sales"))
        
category_df = category_df.orderBy(["product_category"])

# Add file
category_by_country_path = Path(__file__).parent / "data/oluwatobi/category_by_country.csv"
df.toPandas().to_csv(str(category_by_country_path), index=False)

category_path = Path(__file__).parent / "data/oluwatobi/category.csv"
category_df.toPandas().to_csv(str(category_path), index=False)

county_max_total_sale_path = Path(__file__).parent / "data/oluwatobi/county_max_total_sale.csv"
county_max_total_sale_df.toPandas().to_csv(str(county_max_total_sale_path), index=False)

county_max_unit_sold_path = Path(__file__).parent / "data/oluwatobi/county_max_unit_sold.csv"
county_max_unit_sold_df.toPandas().to_csv(str(county_max_unit_sold_path), index=False)

"""For jupyter
path = os.path.abspath('') + "/category_by_country"
df.write.csv('file://'+str(path), header=True) """