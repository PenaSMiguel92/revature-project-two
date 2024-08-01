# import the users.json file
import json
import random



def customer_details():
    with open('./data/users.json') as f:
        users = json.load(f)
    user = random.choice(users)
    return {
         "id": user["id"],
        "full_name": user["full_name"],
        "city": user["city"],
        "country": user["country"]
    }
