import json
import requests
from decimal import Decimal

def get_json_data():
    try:
        return requests.get('http://192.168.1.2/t.json')
    except requests.HTTPError as err:
        print(err)

def post_json_data():
    resp = get_json_data().json()
    
    data = json.dumps(resp)
    
    requests.post('http://127.0.0.1:8000/boiler/post/', json=data)    

post_json_data()