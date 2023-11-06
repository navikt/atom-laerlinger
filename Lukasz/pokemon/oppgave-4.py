import requests

pokemon54 = requests.get("https://pokeapi.co/api/v2/pokemon/54")
pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/3")


pokemon54_height=pokemon54.json()["height"]
pokemon54_weight=pokemon54.json()["weight"]

pokemon3_height=pokemon3.json()["height"]
pokemon3_weight=pokemon3.json()["weight"]


print (pokemon3_height > pokemon54_height)
print (pokemon3_weight > pokemon54_weight)


if pokemon3_weight > pokemon3_weight:
    print("pokemon3 weier mer enn pokemon54")
else:
    print("pokemon54 weier mer enn pokemon3")

if pokemon3_height > pokemon3_height:
    print("pokemon3 er høyere enn pokemon54")
else:
    print("pokemon54 er høyere enn pokemon3")


temperaturen = 30

if temperaturen < 0:
    print("Det er frysepunktet, kle deg varmt.")

if temperaturen > 0 and temperaturen < 15:
    print("Det er kjølig, ta på en jakke.")

if temperaturen > 16 and temperaturen < 25:
    print("Det er behagelig, nyt været.")

if temperaturen > 25:
    print("Det er varmt, tid for shorts og T-skjorte.")