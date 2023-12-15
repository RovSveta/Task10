import json

with open('countries.json') as f:
    countries = json.load(f)

for country in countries:
    print(f"{country['country']}: {country['capital']}")


