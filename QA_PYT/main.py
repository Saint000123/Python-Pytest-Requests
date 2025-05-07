import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '93f5c29fd99962d12c79070e580d909d'
HEADER = {'Content-type' : 'application/json','trainer_token':TOKEN }
body_registration = {
    "name": "Бульбазавр",
    "photo_id": 1 ,
    
}
body_comfirmation = {
    "pokemon_id": "309858",
    "name": "Лучик",
    "photo_id": 87
}
body_create = {
    "pokemon_id": "309858"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_comfirmation)
print(response_confirmation.text)
'''
response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response_create.text)