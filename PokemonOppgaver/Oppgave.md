# Python Oppgaver: Utforske PokeAPI
[Les mer om PokéApi her](https://pokeapi.co)

[PokéApi dokumentasjon](https://pokeapi.co/docs/v2#pokemon-section)
```bash
url: https://pokeapi.co/api/v2/pokemon/{id}/
```
## Oppgave 1: Hente og vise grunnleggende informasjon

**Mål:** Hente grunnleggende informasjon om en gitt Pokémon fra PokeAPI.

1. Skriv en funksjon som tar inn et Pokémon's id.
2. Bruk funksjonen til å hente Pokémonens navn, type, høyde, og vekt.
3. Skriv ut informasjonen i en pent formatert måte.

Tips:

Utforsk API-dokumentasjonen for å forstå hvordan du kan hente informasjon om en Pokémon ved hjelp av dens ID.
Bruk en HTTP-klient i Python, som `requests`, for å sende en GET-forespørsel til API-endepunktet.
Ta en titt på responsen fra API-en og identifiser feltene som inneholder `navnet`, `typer`, `høyden` og `vekten` til Pokémonen.
Lag en pent formatert utskrift ved hjelp av Python sin `print()` funksjon.

Input:
```
24
```
Resultat:
```
Name: Arbok
Height: 35
Weight: 650
Types: Poison
```

---

## Oppgave 2: Vis alle typer Pokémon

**Mål:** Liste opp alle forskjellige typer Pokémon fra PokeAPI.

1. Bruk API-endepunktet for å hente en liste over alle Pokémon-typer.
2. Skriv ut hver type i en liste.

Tips: 
Undersøk API-dokumentasjonen for å finne ut hvilket endepunkt som gir en liste over alle Pokémon-typer.
Bruk Python sin `requests` modul for å sende en GET-forespørsel til det relevante endepunktet.
Analyser responsen for å identifisere feltet som inneholder listen over Pokémon-typer.
Bruk en `for-loop` til å skrive ut hver type i en liste.

Resultat:
```
Available types: Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy, Unknown, Shadow
```
---

## Oppgave 3: Hente Pokémon basert på type

**Mål:** Hente en liste over alle Pokémon av en bestemt type.

1. Skriv en funksjon som tar inn en Pokémon-type.
2. Bruk funksjonen til å hente en liste over alle Pokémon av den typen.
3. Skriv ut navnene på alle Pokémon i listen.

Tips:

Utforsk API-dokumentasjonen for å finne ut hvordan du kan hente en liste over alle Pokémon av en bestemt type.
Lag en funksjon som tar inn en Pokémon-type som parameter og sender en GET-forespørsel til det relevante API-endepunktet.
Analyser responsen for å identifisere feltet som inneholder listen over Pokémon.
Bruk en løkke til å skrive ut navnene på alle Pokémon i listen.

Input:
```
electric
```
Resultat:
```
Pokemons of type Electric: Pikachu, Raichu, Magnemite, Magneton, Voltorb, Electrode, Electabuzz, Jolteon, Zapdos, Chinchou, Lanturn, Pichu, Mareep, Flaaffy, Ampharos, Elekid, Raikou, Electrike, Manectric, Plusle, Minun, Shinx, Luxio, Luxray, Pachirisu, Magnezone, Electivire, Rotom, Blitzle, Zebstrika, Emolga, Joltik, Galvantula, Tynamo, Eelektrik, Eelektross, Stunfisk, Thundurus-Incarnate, Zekrom, Helioptile, Heliolisk, Dedenne, Charjabug, Vikavolt, Togedemaru, Tapu-Koko, Xurkitree, Zeraora, Yamper, Boltund, Toxel, Toxtricity-Amped, Pincurchin, Morpeko-Full-Belly, Dracozolt, Arctozolt, Regieleki, Pawmi, Pawmo, Pawmot, Tadbulb, Bellibolt, Wattrel, Kilowattrel, Sandy-Shocks, Iron-Hands, Iron-Thorns, Miraidon, Rotom-Heat, Rotom-Wash, Rotom-Frost, Rotom-Fan, Rotom-Mow, Thundurus-Therian, Ampharos-Mega, Manectric-Mega, Pikachu-Rock-Star, Pikachu-Belle, Pikachu-Pop-Star, Pikachu-Phd, Pikachu-Libre, Pikachu-Cosplay, Pikachu-Original-Cap, Pikachu-Hoenn-Cap, Pikachu-Sinnoh-Cap, Pikachu-Unova-Cap, Pikachu-Kalos-Cap, Pikachu-Alola-Cap, Raichu-Alola, Geodude-Alola, Graveler-Alola, Golem-Alola, Vikavolt-Totem, Oricorio-Pom-Pom, Pikachu-Partner-Cap, Togedemaru-Totem, Pikachu-Starter, Pikachu-World-Cap, Toxtricity-Low-Key, Morpeko-Hangry, Pikachu-Gmax, Toxtricity-Amped-Gmax, Toxtricity-Low-Key-Gmax, Voltorb-Hisui, Electrode-Hisui, Miraidon-Low-Power-Mode, Miraidon-Drive-Mode, Miraidon-Aquatic-Mode, Miraidon-Glide-Mode
```
---

## Oppgave 4: Sammenligne to Pokémon

**Mål:** Sammenligne vekt og høyde av to forskjellige Pokémon.

1. Skriv en funksjon som tar inn navnene på to Pokémon.
2. Hent vekt og høyde for begge Pokémon.
3. Sammenlign vekt og høyde og skriv ut hvilken Pokémon som er tyngre og hvilken som er høyere.

Input:
```
54 og 3
```
Resultat:
```
Venusaur is taller than Psyduck.
Venusaur is heavier than Psyduck.
```
---

## Oppgave 5: Lag en interaktiv PokeDex

**Mål:** Lag et interaktivt program som lar brukeren søke etter Pokémon og se deres detaljer.

1. Programmet skal ha en hovedmeny der brukeren kan velge forskjellige handlinger (f.eks. søke etter Pokémon, liste alle typer, avslutte).
2. Implementer søkefunksjonalitet som lar brukeren skrive inn et Pokémon-navn og se detaljert informasjon om den.
3. Brukeren skal kunne avslutte programmet ved å velge en "exit" handling.

Resultat:
```
1. Get Pokemon info
2. List all types
3. Get Pokemon by type
4. Compare two Pokemon
5. Exit
Enter your choice: 
```
---

## Bonusoppgave: Lagre Pokémon-informasjon lokalt

**Mål:** For å unngå å hente data fra API-en hver gang, kan du lagre Pokémon-informasjon lokalt.

1. Når brukeren henter informasjon om en Pokémon, lagre denne informasjonen i en lokal fil.
2. Neste gang brukeren søker etter samme Pokémon, hent informasjonen fra den lokale filen i stedet for API-en.
3. Legg til en "oppdater data" funksjon som lar brukeren oppdatere den lagrede informasjonen ved å hente den på nytt fra API-en.

