import requests
import json

URL = 'http://127.0.0.1:8000/StudentApi/'

req = requests.get(url= URL)

print(req.json())
