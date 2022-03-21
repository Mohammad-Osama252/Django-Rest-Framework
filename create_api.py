import requests
import json

URL = 'http://127.0.0.1:8000/createStudent/'

data = {
    'name': 'Hamza',
    'roll': 2,
    'city': 'Lahore'
}

json_data = json.dumps(data)

req = requests.post(url = URL, data = json_data)
data = req.json()
print(data)


# def update():
#
#     data = {
#         'id': 4,
#         'name': 'Taha',
#         'city': 'Quetta'
#     }
#
#     json_data = json.dumps(data)
#
#     req = requests.put(url=URL, data=json_data)
#     data = req.json()
#     print(data)
#
# update()


def delete():

    data = {'id': 2}

    json_data = json.dumps(data)

    req = requests.delete(url=URL, data=json_data)

    print(req.json())


# delete()