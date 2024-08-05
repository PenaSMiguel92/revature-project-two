import json
import random

websites = {'petsmart.com':'everything', 'amazon.com': 'everything', 'chewy.com': ['meds','food','toy'],
'onpdg.com': ['bed', 'crates', 'leash']}

#Open File
with open('./data/products.json') as f:
    items: dict = json.load(f)
catalogs: dict = dict()

# Add item to website catalog
def add_item(key, product):
    if key in catalogs.keys():
        items: list = catalogs[key]
        items.append(product)
    else:
        catalogs[key] = [product]

# Create catlog
for item in items:
    product = {}
    product['product_id'] = item['product_id']
    product['category'] = item['category']
    product['name']  = item['name']
    price_range = item['price_range']
    category = product['category']
    for key in websites.keys():
        categories = websites[key]
        product['price']  = round(random.uniform(price_range[0],price_range[1]), 2)
        if categories == 'everything':
            add_item(key,product)
        elif category in categories:
            add_item(key,product)

# Define the output file name
output_file = './data/catalogs.json'

# Write the user data to a JSON file
with open(output_file, 'w') as f:
    json.dump(catalogs, f, indent=4)

print(f"Generated {len(catalogs)} catlogs and saved to {output_file}")