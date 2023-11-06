
""" import requests

x = requests.get('https://w3schools.com')
print(x.status_code) 
"""

import requests

# Oppgave 1 Hente og vise grunnleggende informasjonpip u
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/666")
print("Type "+(response.json()["types"][0]["type"]["name"]))
print("Name "+(response.json()["name"]))
print("Hieght ", (response.json()["height"]))
print("Weight ", (response.json()["weight"]))


import requests


response = requests.get("https://pokeapi.co/api/v2/type")


print("type", response.json()["results"][0]["name"])
print("type", response.json()["results"][1]["name"])
print("type", response.json()["results"][2]["name"])
print("type", response.json()["results"][3]["name"])
print("type", response.json()["results"][4]["name"])
print("type", response.json()["results"][5]["name"])
print("type", response.json()["results"][6]["name"])
print("type", response.json()["results"][7]["name"])
print("type", response.json()["results"][8]["name"])
print("type", response.json()["results"][9]["name"])
print("type", response.json()["results"][10]["name"])
print("type", response.json()["results"][11]["name"])
print("type", response.json()["results"][12]["name"])
print("type", response.json()["results"][13]["name"])
print("type", response.json()["results"][14]["name"])
print("type", response.json()["results"][15]["name"])
print("type", response.json()["results"][16]["name"])
print("type", response.json()["results"][17]["name"])