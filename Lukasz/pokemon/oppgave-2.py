import requests

response = requests.get("https://pokeapi.co/api/v2/type")




for type in response.json()["results"]:
    print(type["name"])


countries = ["Norway", "Sweden", "Denmark", "Finland", "Iceland", 
    "United States", "Canada", "Mexico", "Brazil", "Argentina", "China", 
    "Japan", "South Korea", "India", "Australia", "New Zealand", "Russia",
    "Germany", "France", "United Kingdom"]
counter = 0
for i, country in enumerate(countries):
    print (i, country)
    counter = counter + 1

print(countries.count("Norway"))
print(counter)