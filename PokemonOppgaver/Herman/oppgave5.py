
#1. Get Pokemon info
#2. List all types
#3. Get Pokemon by type
#4. Compare two Pokemon
#5. Exit
#Enter your choice: 


import requests


#pokemonice = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/ice")
#pokemonfairy = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/fairy")
#pokemonghost = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/ghost")
#pokemondragon = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/dragon")
#pokemonelectric = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/electric")
#pokemonsteel = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/steel")
#pokemonrock = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/rock")
#pokemonground = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/ground")
#pokemondark = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/dark")
#pokemonfighting = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/fighting")
#pokemonpoison = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/poison")
#pokemonfire = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/fire")
#pokemonbug = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/bug")
#pokemonpsychic = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/psychic")
#pokemonflying = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/flying")
#pokemongrass = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/grass")
#pokemonnormal = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/normal")
#pokemonwater = requests.get(f"https://pokeapi.co/api/v2/pokemon/type/water")

import requests

type = input("enter pokemon type")

url = f"https://pokeapi.co/api/v2/type/{type}"

response = requests.get(url).json()

pokemon_list = response["pokemon"]

for pokemon in pokemon_list: print(pokemon["pokemon"]["name"])

