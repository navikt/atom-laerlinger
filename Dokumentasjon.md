# Lærlingnotater

Lærlingene oppfordres til å fordype seg i hvert av disse emnene, stille spørsmål og dele sin forståelse med andre. Notatene kan også inkludere eksempler, kodeutdrag og praktiske øvelser for å styrke læringen. Dette dokumentet er en ressurs for å hjelpe lærlingene i deres utdanningsreise.

## Uke 1: Introduksjon til Python

•	Python Oppgaver
o	Gjennomgikk oppgavene i Python-programmering.
løste 4 oppgaver grunnleggende oppgaver.
Vi lærte å programmere i Python med enkeltoppgaver
hver oppgave viste hva vi kunne gjøre i Python

**oppgave 1: hello world**

Print helloworld og lukasz      
```
print('Hello World ' + 'Lukasz')
```


**oppgave 2: if-else**

Bruker blir sport om input. 
Hvis input er under 18.     
Hrint i terminalen du er under 18 år gammel.
Hvis input er over 18.
Print du er over 18 år gammel.       
Hvis input er lik 18.        
Print du er 18 år gammel.        
```

age = int(input('Hvor gammel er du? '))
if age < 18:
    print('du er under 18 år gammel')
if age > 18:
    print('du er over 18 år gammel')
if age == 18:
    print('du er 18 år gammel')
```

**oppgave 3: lister**
    
Terminalen printer ut nummerene 1, 5, 102, 9, 42 i terminalen.
```
numbers = [1,5, 102, 9, 42]
for numbers in numbers:
    print(numbers)
```

**oppgave 4: løkker**


Detter er en for løkke og den printer alle nummerene som er bestemt.                
I dette tilfelle printer terminalen ut nummerene fra til 11.
```

for i in range(1, 11):
    print(i)
```

o	Lærte grunnleggende konsepter som funksjoner, for-løkker og datatyper.
Det første vi gikk igjennom var hello world, if-else, løkker, lister og githandlinger
o	Diskuterte bruken av APIer.
Du kan hente data fra nett som vi gjorde på Pokemon oppgaven. 
Bruker mye mindre data kraft fordi du ikke har en ful database sående på din locale pc.
Vi brukt API for å hente informasjon og ikke skive all koden på nytt


## Uke 2: Introduksjon til Verktøy og Systemer

•	Rest Python Oppgave
løste 5 Pokemon oppgaver.

<<<<<<< HEAD
oppgave 1: lærte hvordan importere data fra en api    

oppgave 2: lærte hvordan hente relevant data fra en api   

oppgave 3: lærte hvordan hente type                       

oppgave 4: lærte hvordan sammenligne to typer Pokemon         
                  
oppgave 5: lagde en applikasjon med en menu,                        
=======
**oppgave 1: lærte hvordan importere data fra en api**

Jeg har skrevet inn en link om hva jeg vil ha. Linken er til pokemon nummer 6. Koden printer ut type, navn, høyden og vekten til pokemn nummer 6 i rekkefølge.
```
import requests     
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/6")     
print("type" , response.json()["types"][0]["type"]["name"])        
print("navn " + ( response.json()["name"]))     
print("height" , response.json()["height"])     
print("weight" , response.json()["weight"])     
```

**oppgave 2: lærte hvordan hente relevant data fra en api**

Jeg har skrevet inn en lenke hvor den reffererer til alle type pokemon. Det treminalen printer ut er alle de forsjelige type pokeon som finnes.
```
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
```
**oppgave 3: lærte hvordan hente type**
Jeg har laget en variabel som skal prine ut alle pokemon som er av typen electric.

import requests

type = "electric"

url = f"https://pokeapi.co/api/v2/type/{type}"

response = requests.get(url).json()

pokemon_list = response["pokemon"]

for pokemon in pokemon_list: print(pokemon["pokemon"]["name"])


```
**oppgave 4: lærte hvordan sammenligne to typer Pokemon**

I denne oppgaven så printer terminaen ut de to første påstandene er riktige og at venusaurer er tyngre og høyere en psyduck. Dette har vi gjort med hjelp av if else koder. Det er ogs en til kode eksempel hvor vi har brukt if else koder til å beregne om hvor mye klær man skal a på seg i de sesefike tempraturere.

```
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
```
**oppgave 5: lagde en applikasjon med en menu,**
```

I oppgve 5 så har jeg lagt et program om alt vi har lært v de forje oppgavene. Treminalen spørr deg om hvilken pokemon du har lyst tl å se. For Eksempel hvis du putter inn fire så får du opp en lise over alle pokemoene som er av typen fire.




(Eksempel 1)
import requests

type = input("enter pokemon type")

url = f"https://pokeapi.co/api/v2/type/{type}"

response = requests.get(url).json()

pokemon_list = response["pokemon"]

for pokemon in pokemon_list: print(pokemon["pokemon"]["name"])




(Eksempel 2)
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
    userpokemon = input("Hvilken pokemon letter du etter? ")
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

    pokemon54 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{usertype1}")
    pokemon3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{usertype2}")


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
    print("bye")
    exit()




```
>>>>>>> e19d76866772b919dc1c89ae9bf7f32e6550ffaa

•	Git og GitHub

o	Forklart Git som et versjonskontrollsystem.
Fikk en forklaring på hva GitHub er og hvordan vi skal bruke det i arbeidet vårt.
Vi bruke GitHub for å dele filer med hverandre over internettet istedenfor å sende dem på mail.

o	Demonstrert forskjellen mellom lokale og eksterne (remote) repositorier.
Locale repositries kan være at du lagrer filene dine lokalt på pcen din og å lagre ting remote kan være å laste det opp til en server eller git hub sånn at alle team medlemmene kan få tilgang til med.

o	Skissert prosessen for å pushe kode til et Git-repo.
Jeg pushet koden til git hub sånn at Lukasz kunne se kodene og finne ut hva vi gjorde annerledes får å løse en oppgave.

Jira
•	Lastet ned Jira på oppsatt RHEL maskin.
Lastet ned jira fra browser og lastet det opp på Linux serveren og begynte å konfigurere den opp.


## Uke 3: Systemadministrasjon og Verktøy

•	Installasjon av Jira
o	Gitt veiledning om Jira-installasjon med fokus på konfigurasjon og endringer i konfigurasjonsfiler.
Jeg fikk lære og gjennomgått hvordan man navigerer seg i Linux og hvordan Linux er satt opp.
•	Brannmur og Serverbestillinger
o	Undersøkt lett formålet med brannmurer i nettverkssikkerhet.
Den største fordelen for brukere er bedre sikkerhet. Ved hjelp av en brannmur setter du opp et sikkerhetsnett som kan bidra til å beskytte datamaskinen eller nettverket mot skadelig innkommende trafikk. Denne teknologien kan også filtrere skadelig utgående trafikk. (https://www.eset.com/no/firewall/) kilde.
o	Diskutert hvordan man bestiller og konfigurerer servere, inkludert RAM, CPU og OS-krav.
Vi bestilte alt ved hjelp av Basta. Vi bestilte det minste vi kunne bestille for i trengte ikke mer og utifra det dockumente sa
•	Linux Kommandoer og Filstruktur
o	Lært viktige Linux-kommandoer og deres bruksområder.
Laget et Word-dokument over viktige Linux kommandoer
Kommando	Nøkkelord	Beskrivelse
ls	Liste (Directory conteent)	Viser innholdet i mappen du sår i   
cd		Changes the working dirctorys path
Cp fra_fil til_fil	Copy	Kopierer en fil fra et sted til et annet
Mv fra_fil til_fil	Move	Flytter en fil fra et sed til et annet
Mkdir mappenavn	Make dirctory	Lag n ny mappe
Rm filnavn	remove	Slett fil(rm-d for å slette en mappe)
pwd	Print working directory	Viser sti til mapen du står i
chmod	Change mode	Endre rettightene tile n fil/mappe (se man chmod)
Chgrp gruppenavn filnavn	Change group endre 	Endre gruppen tle en fil/mappe
useradd	Creats user	Lenger n ny bruker
userdel	Removes user	Sletter en ny bruker
man kommando	Manual	Viser manualsidene til komandoen (q for å avslute)
ssh «brukernavn»@»Servernavn»	Secure shell	Åpner en secure shell tilkobling til serveren
Touch»filnavn»		Lager en fil med navn «filnavn»
Rm	Deletes	Delees a file
File		Skjekker hvilken type fil det er
Sudo	Superuser	Runs a comand as a superuser
Su 	Another user	Runs programs in the current shell as another user
Chown		Changes a files, directory, or symbolic link’s ownership
Top 	System’s resource usage	Displays running processes and the sysem’s resource usage.
Kill	Terminate	Terminates a running process
Shutdown	Turn off/ restart	
History	Check history	Lists previously run commands
Man	Command’s manual	
		
		




	

o	Utforsket filstrukturer og beste praksis for organisering.
Vi hadde en prat om det og når vi lager en cluster struktur som vi gjorde. Og man bruker to helt like noder burde man konfigurere dem opp helt likt sånn at det ikke blir noe forvirring på hvor ting ligger. Det er også positivt å gjøre det på en ryddig og fin måte slik at når noen tar over eller hjelper deg blir det ikke forvirrende og vanskelig å jobbe med dem.











## Uke 4: Avanserte Emner

•	NFS (Network File System)
o	Utforsket NFS og dens rolle i deling av filer over et nettverk.
Network file system deler filer fra databasen til pcer som er i samme Nettverk. Brukere kan få tak i remote systemer slik som om de var fra lokal-pc. Lokale PCer kan spare diskplass fordi filer blir lagret på serveren istedenfor locale maskiner. Vi kan bruke lagrings enheter som for eks USB minnebrikke, da kan andre maskiner koble seg opp til NFS og bruke dem uten å gå fysisk til serveren.
[Kilde](https://ubuntu.com/server/docs/service-nfs). 

Nfs har ikke noe driekte mulighet for å spare disk plass.
Det er et felles område hvor alle kan hene informasjon som alle skal ha ilgang til.
Ha et felles område som alle serverene skal bruke
Legge det i slack kanalen sånn at alle kan se det istedn for å sende individuelle opptateringer eller ha et møte.
Når mann kjøre et kløster kan man oppkradere den en server ved å ta ned den ene og kjøre krafen på den andre sånn at nettsiden slipper å gå ned. Når den første er ferdig oppkradert kan man oppkradere den andre uten problemer.
vi skal finne ut hvrdan v legger til filene til vårt atomrepoet. lage en ny fil g legge inn dukumentasjonen.

•	Jira Cluster
o	Forstått fordelen med å ha et Jira-cluster for økt pålitelighet.
Forstått fordelen med å ha et Jira-cluster for økt pålitelighet. 
Hvis den ene noden slutter å funke så funker fortsatt den andre og nettsiden går ikke ned. 
Et cluster kan ha mer brukere enn en server kan. 

o	Diskutert nødvendige ekstra ressurser for å implementere et Jira-cluster.
For å ha et jira-cluster så må vi ha en 2 noder, network shared file system, load balancer og shared database. 
•	Automatisering Ikke gjennomgått
o	Utforsket automatisering og dens betydning.
Slipper å konfigurere nye enheter til clustere manuelt. Slipper å gjøre feil.  
Bruke load balancer for å justere hvor mye datakraft clusteren bruker til enhver tid. Dette er positivt, fordi du bruker bare den kraften du trenger, istedenfor å betale for datakraften som ikke er i bruk. 
lode balancer har ikke noe med datakrat. Hensikten med last balansereren er å fordele data traffiken ikke datakraften . Den fordele lasten på serverene. Hvis den automatisk slår av en server tar den andre noden datatraffiken. Kunn trafikk flyt bruker man lastbalansereren ikke serverkraft.

o	Presentert trinn for trinn hvordan man automatiserer oppsettet av Jira for effektiv drift.
Har ikke gjennomgått.




[Kilde](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

det skal være en
 
det første steget 
git add filen som er endret(tips bruk git satus for å se hvilken fil som er endret)
git commit -m "meldingen" 
git push for å dyte det inn