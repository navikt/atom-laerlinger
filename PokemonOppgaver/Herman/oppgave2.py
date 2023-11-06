import requests

response = requests.get("https://pokeapi.co/api/v2/type")

# Lag en liste av resultater fra responsen
results = response.json()["results"]

# Bruk en for-loop for å gå gjennom listen
for result in results:
    # Skriv ut navnet på hvert resultat
    print("type", result["name"])