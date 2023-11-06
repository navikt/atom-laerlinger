import requests

# Oppgave 1 Hente og vise grunnleggende informasjonpip u
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/6")
print("type" , response.json()["types"][0]["type"]["name"])
print("navn " + ( response.json()["name"]))
print("height" , response.json()["height"])
print("weight" , response.json()["weight"])
