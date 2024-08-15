from pathlib import Path
from datetime import date
import load_csv

def get_popularity_over_year(context):
    query_split_datetime = 'CONCAT(YEAR(datetime), \'_Q\',QUARTER(datetime)) AS year_quarter'
    query_quarters = f'SELECT {query_split_datetime} FROM orders'
    query_unique_quarters = f'SELECT DISTINCT year_quarter FROM ({query_quarters}) ORDER BY year_quarter'
    quarters_df = context.sql(query_unique_quarters)
    quarter_list = quarters_df.collect()
    quarter_list = [row['year_quarter'] for row in quarter_list]

    query_pivot = '('
    for index, quarter in enumerate(quarter_list):
        if index == len(quarter_list) - 1:
            query_pivot += f'\'{quarter}\')'
        else:
            query_pivot += f'\'{quarter}\', '

    query_popularity_over_year_subquery = f'SELECT {query_split_datetime}, product_name, qty FROM orders'
    query_popularity_over_year = f'SELECT * FROM ({query_popularity_over_year_subquery}) PIVOT (SUM(qty) AS popularity FOR year_quarter IN {query_pivot})'

    pop_year_df = context.sql(query_popularity_over_year)
    pop_year_df = pop_year_df.na.fill(0)

    #query total popularity of each product over the year:
    query_total_popularity = f'SELECT product_id, product_name, SUM(qty) AS total_popularity FROM orders GROUP BY product_id, product_name'
    tot_pop_year_df = context.sql(query_total_popularity)
    #get top 10 most popular products:
    pop_year_df = pop_year_df.join(tot_pop_year_df,['product_id', 'product_name']).sort('total_popularity', ascending=False).limit(10)
    # pop_year_df.show()

    # pop_year_df.show(1000)
    return pop_year_df

def get_popularity_over_country(context):
    # Query to get the countries where the top 5 products are sold the most
    query_popularity_over_country = '''
        SELECT country, product_id, product_name, SUM(qty) AS popularity
        FROM orders
        WHERE product_id IN (
            SELECT product_id
            FROM pop_year_df
            ORDER BY total_popularity DESC
            LIMIT 5
        )
        GROUP BY country, product_id, product_name
        ORDER BY product_id, popularity DESC
    '''
    pop_country_df = context.sql(query_popularity_over_country)

    return pop_country_df

def main():
    data_frame = load_csv.load("/data/clean_data.csv")
    context = load_csv.getContext()
    data_frame.createOrReplaceTempView('orders')

    pop_year_df = get_popularity_over_year(context)
    pop_country_df = get_popularity_over_country(context)

    path1 = Path(__file__) / "/data/miguel/popularity_over_year.csv"
    path2 = Path(__file__) / "/data/miguel/popularity_over_country.csv"
    pop_year_df.toPandas().to_csv(str(path1), index=False)
    pop_country_df.toPandas().to_csv(str(path2), index=False)

if __name__ == '__main__':
    """
        Note that this is a standalone script that generates two csv files from the clean data.
    """
    main()