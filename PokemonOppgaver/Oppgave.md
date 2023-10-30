# Python Oppgaver: Utforske PokeAPI

## Oppgave 1: Hente og vise grunnleggende informasjon
[Les mer om PokéApi her](https://pokeapi.co)

**Mål:** Hente grunnleggende informasjon om en gitt Pokémon fra PokeAPI.

1. Skriv en funksjon som tar inn et Pokémon's id.
2. Bruk funksjonen til å hente Pokémonens navn, type, høyde, og vekt.
3. Skriv ut informasjonen i en pent formatert måte.

```bash
url: https://pokeapi.co/api/v2/pokemon/{id}/
```

---

## Oppgave 2: Vis alle typer Pokémon

**Mål:** Liste opp alle forskjellige typer Pokémon fra PokeAPI.

1. Bruk API-endepunktet for å hente en liste over alle Pokémon-typer.
2. Skriv ut hver type i en liste.

---

## Oppgave 3: Hente Pokémon basert på type

**Mål:** Hente en liste over alle Pokémon av en bestemt type.

1. Skriv en funksjon som tar inn en Pokémon-type.
2. Bruk funksjonen til å hente en liste over alle Pokémon av den typen.
3. Skriv ut navnene på alle Pokémon i listen.

---

## Oppgave 4: Sammenligne to Pokémon

**Mål:** Sammenligne vekt og høyde av to forskjellige Pokémon.

1. Skriv en funksjon som tar inn navnene på to Pokémon.
2. Hent vekt og høyde for begge Pokémon.
3. Sammenlign vekt og høyde og skriv ut hvilken Pokémon som er tyngre og hvilken som er høyere.

---

## Oppgave 5: Lag en interaktiv PokeDex

**Mål:** Lag et interaktivt program som lar brukeren søke etter Pokémon og se deres detaljer.

1. Programmet skal ha en hovedmeny der brukeren kan velge forskjellige handlinger (f.eks. søke etter Pokémon, liste alle typer, avslutte).
2. Implementer søkefunksjonalitet som lar brukeren skrive inn et Pokémon-navn og se detaljert informasjon om den.
3. Brukeren skal kunne avslutte programmet ved å velge en "exit" handling.

---

## Bonusoppgave: Lagre Pokémon-informasjon lokalt

**Mål:** For å unngå å hente data fra API-en hver gang, kan du lagre Pokémon-informasjon lokalt.

1. Når brukeren henter informasjon om en Pokémon, lagre denne informasjonen i en lokal fil.
2. Neste gang brukeren søker etter samme Pokémon, hent informasjonen fra den lokale filen i stedet for API-en.
3. Legg til en "oppdater data" funksjon som lar brukeren oppdatere den lagrede informasjonen ved å hente den på nytt fra API-en.

