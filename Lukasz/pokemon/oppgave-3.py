import requests

type = "electric"

url = f"https://pokeapi.co/api/v2/type/{type}"

response = requests.get(url).json()

pokemon_list = response["pokemon"]

for pokemon in pokemon_list: print(pokemon["pokemon"]["name"])