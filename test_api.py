import json

import requests
import random
from faker import Faker

def test_add_pet():
    fake = Faker()
    pet_id = random.randint(1, 99999999)
    input_pet = {
        "id": pet_id,
        "category": {
            "id": random.randint(1, 99999999),
            "name": fake.name()
        },
        "name": fake.name(),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 7,
                "name": fake.name()
            }
        ],
        "status": "available"
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    assert res_post.status_code == 200
    assert res_post.json() == input_pet

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}', headers= {'accept': 'application/json'})
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json() == input_pet

