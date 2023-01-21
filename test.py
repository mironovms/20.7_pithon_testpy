import requests
import json

def test_add_pet():
    input_pet = {
        "id": 228,
        "category": {
            "id": 224,
            "name": "Robik"
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
    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    print('\n', res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url = f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
    assert res_get.status_code == 200
    assert json.loads(res_post.text) == input_pet

def test_sold_list():
    input_pet = {
        "id": 229,
        "category": {
            "id": 225,
            "name": "Xobot"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 54,
                "name": "dog"
            }
        ],
        "status": "sold"
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status' : 'sold'})
    assert res_get.status_code == 200
    assert input_pet in list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))

def test_available_list():
    input_pet = {
        "id": 229,
        "category": {
            "id": 225,
            "name": "Xobot"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 54,
                "name": "dog"
            }
        ],
        "status": "available"
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status' : 'available'})
    assert res_get.status_code == 200
    assert input_pet in list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))


