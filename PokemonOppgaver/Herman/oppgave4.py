import requests

# Få terminalen til å skrive ut navnene på 54 og 3. 

pokemon54 = requests.get(f"https://pokeapi.co/api/v2/pokemon/54")
pokemon3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/3")

# Deretter få inn høyden og vekten på de to forsjelige. 

pokemon54_name=pokemon54.json()["name"]

pokemon54_height=pokemon54.json()["height"]
pokemon54_weight=pokemon54.json()["weight"]


pokemon3_name=pokemon3.json()["name"]

pokemon3_height=pokemon3.json()["height"]
pokemon3_weight=pokemon3.json()["weight"]

# Dereter skrive noe kode som karer å bestemme hvilken av verdiene sm er størst og minst. høyde og vekt
#if weight mer en den andre print psyduck er lavere enn 3.
#else height mer en den andre print 3 er tyngre enn 54.
print (pokemon3_weight > pokemon54_weight)
print (pokemon3_height > pokemon54_height)


# Deretter få inn høyden og vekten på de to forsjelige. 

if pokemon3_weight > pokemon54_weight:
    print(f'{pokemon3_name}er tyngre enn {pokemon54_name}.')
else:
    print(f'{pokemon54_name} er tyngre enn {pokemon3_name}.')

if pokemon3_height > pokemon54_height:
    print(f'{pokemon3_name} er høyere enn {pokemon54_name}.')
else:
    print(f'{pokemon54_name} er høyere enn {pokemon3_name}.')