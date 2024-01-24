
# Gjøre HTTP Forespørsler i Python med `requests`

## Innholdsfortegnelse

- [Introduksjon](#introduksjon)
- [Installasjon](#installasjon)
- [Grunnleggende Bruk](#grunnleggende-bruk)
  - [GET Forespørsel](#get-forespørsel)
  - [POST Forespørsel](#post-forespørsel)
- [Avanserte Funksjoner](#avanserte-funksjoner)
  - [Håndtering av Headers](#håndtering-av-headers)
  - [Timeouts](#timeouts)
- [Feilhåndtering](#feilhåndtering)
- [Konklusjon](#konklusjon)

## Introduksjon

`requests` er et populært Python-bibliotek brukt for å sende HTTP-forespørsler. Det er kjent for sin enkelhet og evnen til å håndtere komplekse forespørsler med minimal kode.

## Installasjon

Før du begynner, må du installere `requests`-biblioteket. Dette kan gjøres ved å kjøre følgende kommando:

```bash
pip install requests
```

## Grunnleggende Bruk

### GET Forespørsel

For å sende en GET-forespørsel, bruk `get`-metoden:

```python
import requests

response = requests.get('https://api.example.com/data')
print(response.text)
```

### POST Forespørsel

For å sende en POST-forespørsel, bruk `post`-metoden:

```python
import requests

data = {'key': 'value'}
response = requests.post('https://api.example.com/submit', data=data)
print(response.text)
```

## Avanserte Funksjoner

### Håndtering av Headers

Du kan tilpasse headers for en forespørsel:

```python
import requests

headers = {'User-Agent': 'My App/1.0'}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Timeouts

For å unngå å henge på en forespørsel for lenge, kan du spesifisere en timeout:

```python
import requests

response = requests.get('https://api.example.com/data', timeout=5)
```

## Feilhåndtering

Det er viktig å håndtere potensielle feil, som nettverksproblemer eller 4xx/5xx-responskoder:

```python
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')
```

## Konklusjon

`requests`-biblioteket tilbyr en enkel måte å gjøre HTTP-forespørsler i Python. Ved å følge disse eksemplene, kan du begynne å integrere HTTP-forespørsler i dine Python-applikasjoner.
