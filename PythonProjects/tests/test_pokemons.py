import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '96a1fa946d6903e2272a40fa6b469b0e'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18385'

def test_status_code():
 respons = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
 assert respons.status_code == 200

def test_trainer_id():
 respons_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
 assert respons_get.json()['data'][0]['trainer_name'] == 'Mercuris'