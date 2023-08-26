import requests

data = {'key': '', 'inn': '6321313849'}
r = requests.get('https://api.checko.ru/v2/company', params=data)
print(r.json())

