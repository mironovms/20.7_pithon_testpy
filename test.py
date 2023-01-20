import requests
import json

def test_add_pet():
    input_pet = {
        "id": 0,
        "category": {
            "id": 224,
            "name": "Dobik"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type' : 'application/json'}
    res = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res)
