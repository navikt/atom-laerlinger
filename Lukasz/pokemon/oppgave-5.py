import requests

response = requests.get("https://pokeapi.co/api/v2/type")





#def option3():
 #   print("Option 3 has been called using function!")



#while option != 0:
#     if option == 1:


        





  #   elif option == 2:
  #          print("Option 2 has been called.")
 #    elif option == 3:
 #         option3()  
#else:
 #    print("Invalid option")


#print()
#menu()
#option = int(input("Enter your option: "))

#print("THANKS FOR USING THIS PROGRAM")



#    Oppgave 5: Lag en interaktiv PokeDex
#Mål: Lag et interaktivt program som lar brukeren søke etter Pokémon og se deres detaljer.

#programmet skal ha en hovedmeny der brukeren kan velge forskjellige handlinger (f.eks. søke etter Pokémon, liste alle typer, avslutte).
#Implementer søkefunksjonalitet som lar brukeren skrive inn et Pokémon-navn og se detaljert informasjon om den.
#Brukeren skal kunne avslutte programmet ved å velge en "exit" handling.

#Resultat:

#1. Get Pokemon info
#2. List all types
#3. Get Pokemon by type
#4. Compare two Pokemon
#5. Exit
#Enter your choice






#hovedmeny for å velge forskjellige handlinger søke etter pokemon, liste alle typer avslutte


#viser til brukeren hva han kan velge
def valg():
    print("1. Get all pokemon info")
    print("2. List all types")
    print("3. Get Pokemon by type")
    print("4. Compare two Pokemon")
    print("5. Exit")

#den gjør at menu blir vist i terminalen
valg()


#spør brukeren hva vil han velge
valg = int(input('hva velger du?'))
#hvis brukeren valgte 1
if valg == 1:
    userpokemon = input("Hvilken pokemon letter du etter?")
    url = f"https://pokeapi.co/api/v2/pokemon/{userpokemon}"
    response = requests.get(url)
    print("type" , response.json()["types"][0]["type"]["name"])
    print("navn " + ( response.json()["name"]))
    print("height" , response.json()["height"])
    print("weight" , response.json()["weight"])


#Hvis brukeren valgte 2
if valg == 2:
    url = f"https://pokeapi.co/api/v2/type"
    response = requests.get(url)
    for type in response.json()["results"]:
        print(type["name"])
        
#Hvis brukeren valgte 3
if valg == 3:
    #velger type som pc skal se etter
    usertype = input('hvilken type pokemon velger du? ')
    url = f"https://pokeapi.co/api/v2/type/{usertype}"
    response = requests.get(url)
    print(response.json()["pokemon"])
    for pokemon in response.json()["pokemon"]: print(pokemon["pokemon"]["name"])
#response = requests.get(url).json()

#pokemon_list = response["pokemon"]





#hvis brukeren valgte 4
if valg == 4:
    #hvilken pokemon velger du?
    usertype1 = input('hvilken type pokemon velger du? ')
    usertype2 = input('hvilken type pokemon velger du? ')

    pokemon54 = requests.get("https://pokeapi.co/api/v2/pokemon/{usertype1}")
pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/{usertype2}")


pokemon54_height=pokemon54.json()["height"]
pokemon54_weight=pokemon54.json()["weight"]

pokemon3_height=pokemon3.json()["height"]
pokemon3_weight=pokemon3.json()["weight"]


print (pokemon3_height > pokemon54_height)
print (pokemon3_weight > pokemon54_weight)


if pokemon3_weight > pokemon54_weight:
    print("pokemon3 weier mer enn pokemon54")
else:
    print("pokemon54 weier mer enn pokemon3")

if pokemon3_height > pokemon54_height:
    print("pokemon3 er høyere enn pokemon54")
else:
    print("pokemon54 er høyere enn pokemon3")




#hvis brukeren valgte 5
if valg == 5:
    print('21')







#søkefunksjonalitet som lar brukeren skrive inn et pokemon-navn og se informasjon om den






# brukeren skal kunne avslutte programmet ved å veldge en "exir" handling.