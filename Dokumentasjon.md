# Lærlingnotater

Lærlingene oppfordres til å fordype seg i hvert av disse emnene, stille spørsmål og dele sin forståelse med andre. Notatene kan også inkludere eksempler, kodeutdrag og praktiske øvelser for å styrke læringen. Dette dokumentet er en ressurs for å hjelpe lærlingene i deres utdanningsreise.

## Uke 1: Introduksjon til Python

•	Python Oppgaver
o	Gjennomgikk oppgavene i Python-programmering.
løste 4 oppgaver grunnleggende oppgaver.
Vi lærte å programmere i Python med enkeltoppgaver
hver oppgave viste hva vi kunne gjøre i Python

**oppgave 1: hello world**
```
print('Hello World ' + 'Lukasz')
```

**oppgave 2: if-else**

```
age = int(input('Hvor gammel er du? '))
if age < 18:
    print('du er under 18 år gammel')
if age > 18:
    print('du er ')
if age == 18:
    print('du er 18 år gammel')
```

**oppgave 3: lister**
```
numbers = [1,5, 102, 9, 42]
for numbers in numbers:
    print(numbers)
```
**oppgave 4: løkker**
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
oppgave 1: lærte hvordan importere data fra en api
oppgave 2: lærte hvordan hente relevant data fra en api
oppgave 3: lærte hvordan hente type 
oppgave 4: lærte hvordan sammenligne to typer Pokemon
oppgave 5: lagde en applikasjon med en menu,

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
Vi bestilte alt ved hjelp av jira.
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
Vi hadde en prat om det og når vi lager en cluster struktur som vi gjorde. Og man bruker to nesten helt like noder burde man konfigurere dem opp helt ikt sånn at det ikke blir nee forvirring å hvor ting ligger. Det er også positivt å gjøre det på en ryddig og fin måte slik at når noen tar over eller hjelper deg blir det ikke forvirrende og vanskelig å jobbe med dem.











## Uke 4: Avanserte Emner

•	NFS (Network File System)
o	Utforsket NFS og dens rolle i deling av filer over et nettverk.
Network file system deler filer fra databasen til pcer som er i samme Nettverk. Brukere kan få tak i remote systemer slik som om de var fra lokal-pc. Lokale PCer kan spare diskplass fordi filer blir lagret på serveren istedenfor locale maskiner. Vi kan bruke lagrings enheter som for eks USB minnebrikke, da kan andre maskiner koble seg opp til NFS og bruke dem uten å gå fysisk til serveren.
[Kilde](https://ubuntu.com/server/docs/service-nfs). 

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

o	Presentert trinn for trinn hvordan man automatiserer oppsettet av Jira for effektiv drift.
Har ikke gjennomgått.


Mer forklaring på hva de grunnlegende kodene er 
Se det dørste greiene jhonas har sent og gåjør det bedre
Hvor vi bestilte serverne med basta bestilte det minste vi kunne bestille for i trengte ikke mer og utifra det dockumente sa.
alt skal være helt likkt mllom nodene 
nfs har ikke noe driekte mde noe med å spare disk plas'
har et felles område hvor alle kan hene informasjon som alle skal ha ilgang til
ha et felles område som alle serverene skal bruke
egge det i slack kanalen sånn at 
når amn kjøre n kløster kan man oppkradere en server med å ta den ene ned og kjøre krafen på den andre sånn når den er ferdig oppkradert kan man oppkradere den adre
fler eksempler på progoppgavene
lode balancer har ikke noe med datakrat. hensikten med last balansereren er å fordele data traffiken ikke datakraftenfordele lastn på serverene. når d  automatisk slår av en servner tar de andre noeene kraften. kunn trafikk flyt bruker man lastbalansereren. legger inne n lelding nr en av serverene. bruker det til traffik flyt ikke fordele serverkraft.
vi skal finne ut hvrdan v legger til filene til vårt atomrepoet. lage en ny fil g legge inn dukumentasjonen.
bonus å formatere filen i github read me filer søke på det. 
dokumenere hvordan vi skal pushe filer til github.

[Kilde](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

det skal være en
 
det første steget 
git add filen som er endret(tips bruk git satus for å se hvilken fil som er endret)
git commit -m "meldingen" 
git push for å dyte det inn


