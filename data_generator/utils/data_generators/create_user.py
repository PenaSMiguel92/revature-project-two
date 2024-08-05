import json
import random

# Create a list of 50 full names
full_names = ["Harry Wallace", "Henry Kissinger", "Marie Curie", "Isaac Newton", "Albert Einstein", "Nikola Tesla", "Thomas Edison", "Galileo Galilei", "Charles Darwin", "Louis Pasteur", "Aristotle", "Plato", "Socrates", "Confucius", "Immanuel Kant", "Friedrich Nietzsche", "Jean-Paul Sartre", "Sigmund Freud", "Carl Jung", "Michel Foucault", "Jacques Derrida", "Gilles Deleuze", "Slavoj Zizek", "Judith Butler", "Simone de Beauvoir", "Hannah Arendt", "Rosa Luxemburg", "Emma Goldman", "Angela Davis", "Noam Chomsky", "Edward Said", "Edward Snowden", "Julian Assange", "Chelsea Manning", "Malala Yousafzai", "Greta Thunberg", "Alexandria Ocasio-Cortez", "Ilhan Omar", "Ayanna Pressley", "Rashida Tlaib", "Kamala Harris", "Elizabeth Warren", "Bernie Sanders", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton", "George H.W. Bush", "Ronald Reagan"]

# Create a list of cities in the US, Mexico, or Canada,
cities = [["Los Angeles", "United States"], ["San Bernadino", "United States"], ["San Antonio", "United States"], ["San Diego", "United States"], ["San Francisco", "United States"], ["San Jose", "United States"], ["Santa Ana", "United States"], ["Seattle", "United States"], ["Spokane", "United States"], ["Tacoma", "United States"], ["Tampa", "United States"], ["Tucson", "United States"], ["Tulsa", "United States"], ["Virginia Beach", "United States"], ["Washington", "United States"], ["Wichita", "United States"], ["Winston-Salem", "United States"], ["Denver", "United States"], ["Albuquerque", "United States"], ["Arlington", "United States"], ["Vancouver", "Canada"], ["Toronto", "Canada"], ["Puerto Vallarta", "Mexico"], ["Tijuana", "Mexico"], ["Portland", "United States"], ["Ensenada", "Mexico"], ["Oaxaca", "Mexico"], ["Guadalajara", "Mexico"], ["Victoria", "Canada"], ["Phoenix", "United States"], ["Scottsdale", "United States"], ["Sedona", "United States"], ["Flagstaff", "United States"], ["Las Vegas", "United States"], ["Henderson", "United States"], ["Reno", "United States"], ["Carson City", "United States"], ["Salt Lake City", "United States"], ["Provo", "United States"], ["Ogden", "United States"], ["St. George", "United States"], ["Boise", "United States"], ["Nampa", "United States"], ["Meridian", "United States"], ["Idaho Falls", "United States"], ["Coeur d'Alene", "United States"], ["Caldwell", "United States"], ["Moscow", "United States"], ["Pocatello", "United States"], ["Twin Falls", "United States"]]
# Create a list to hold the user data
users = []

# Generate 50 users
for i in range(1, 51):
    random_city = random.choice(cities)
    user = {
        "id": i,
        "full_name": random.choice(full_names),
        "city": random_city[0],
        "country": random_city[1]
    }
    users.append(user)

# Define the output file name
output_file = './data/users.json'

# Write the user data to a JSON file
with open(output_file, 'w') as f:
    json.dump(users, f, indent=4)

print(f"Generated {len(users)} users and saved to {output_file}")
