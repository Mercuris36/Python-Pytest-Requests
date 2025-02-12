import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96a1fa946d6903e2272a40fa6b469b0e'
HEADERS = {'Content-Type' : 'application/json',
 'trainer_token' : TOKEN}

body_create = {
    "name": "Cтас36",
    "photo_id": 2
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create)
print(response_create.json())

pokemon_id = response_create.json().get('id')
print(pokemon_id)

body_put = {
    "pokemon_id": pokemon_id,
    "name": "NewNewNew2",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": pokemon_id
}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_put)
print(response_put.json())

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_catch)
print(response_catch.json())