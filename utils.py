import requests


BASE_URL = 'https://icanhazdadjoke.com'

def dad_joke():
    json_headers = {'Accept': 'application/json'}
    response = requests.get(BASE_URL, headers=json_headers)
    data = response.json()
    return data['joke']
