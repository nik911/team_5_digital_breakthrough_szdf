
import requests

r = requests.post(
    "https://api.deepai.org/api/logo-generator",
    data={
        'text': 'IT company',
    },
    headers={'api-key': ''}
)
print(r.json())
