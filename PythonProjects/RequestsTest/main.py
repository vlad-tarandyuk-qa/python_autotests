import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e09d44ebc99fb84a62337020d03e5954'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "Vasiliy",
    "photo_id": 12
}

body_change = {
    "pokemon_id": "155416",
    "name": "Babochka",
    "photo_id": 12
}

body_add_pokemons = {
    "pokemon_id": "155416"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)


response_charge = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_charge.text)


responce_add_pokemons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokemons)
print(responce_add_pokemons.text)