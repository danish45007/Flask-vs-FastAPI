import requests

base_url = "http://127.0.0.1:8000"
endpoint = f'{base_url}/box-ofiice-mojo'

res = requests.post(endpoint, json={})
print(res.text)