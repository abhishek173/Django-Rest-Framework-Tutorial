import requests
import json

URL = "http://localhost:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data={'id':id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)

    r =  requests.get(url=URL,headers=headers,data=json_data)

    data = r.json()

    print(data)

# get_data(2)
# get_data()

def post_data():
    data = {
        'name':'Ray',
        'roll': 88,
        'city':'Ranchi'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data = {
        'id':5,
        'name':'Jack',
        'roll':105,
        'city':'Ranchi'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id':5
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# delete_data()
