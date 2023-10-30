# Installasjon

### Python

1. Gå til [Python sin offisielle nettside](https://www.python.org/).
2. Last ned den nyeste versjonen av Python.
3. Åpne den nedlastede filen og følg installasjonsinstruksjonene.

### Git

1. Gå til [Git sin offisielle nettside](https://git-scm.com/).
2. Last ned den nyeste versjonen av Git.
3. Åpne den nedlastede filen og følg installasjonsinstruksjonene.

# Oppgaver

#### Oppgave 1: Hello World

Skriv et Python-program som skriver ut 'Hello World' til konsollen.

```python
print('Hello World' + 'Navn')
# Resultat:
# Hello World Navn
```
#### Oppgave 2: If-else
Skriv et Python-program som spør brukeren om alderen deres og skriver ut om de er under eller over 18 år gammel.

```python
age = int(input('Hvor gammel er du? '))
if age < 18:
    print('Du er under 18 år gammel.')
else:
    print('Du er 18 år eller eldre.')
    
# Input:
# 12

# Resultat:
# Du er under 18 år gammel.
```
#### Oppgave 3: Løkker
Skriv et Python-program som skriver ut tallene fra 1 til 10 ved hjelp av en løkke.

```python
for i in range(1, 11):
    print(i)

# Resultat:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
````

#### Oppgave 4: Lister
Skriv et Python-program som oppretter en liste med tallene fra 1 til 5, og deretter skriver ut hvert tall i listen.

```python

numbers = [1, 5, 102, 9, 42]
for number in numbers:
    print(number)

# Resultat:
# 1
# 5
# 102
# 9
# 42
```
#### Git Handlinger
Etter hver oppgave, lagre endringene dine i Git ved å bruke følgende kommandoer:

Åpne terminalen og naviger til mappen der filen din er lagret.
Skriv inn følgende kommandoer:
```bash
git add .
git commit -m 'Løste oppgave X'
git push

# Erstatt 'X' med nummeret på oppgaven du har løst.
```
