import json
import random
import secrets

def product_purchase_details():
    with open('./data/catalogs.json') as f:
        catalogs:dict = json.load(f)
    websites_name = []
    for key in catalogs.keys():
        websites_name.append(key)
    key = random.choice(websites_name)
    catalog = catalogs[key]
    product:dict = random.choice(catalog)
    product['website'] = key
    product['quantity'] = secrets.randbelow(16)
    return product

print(product_purchase_details())