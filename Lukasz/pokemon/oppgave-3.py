import requests

response = requests.get("https://pokeapi.co/api/v2/type/3")


response = requests.get("https://pokeapi.co/api/v2/pokemon/6")
print("type" , response.json()["types"][0]["type"]["name"])


