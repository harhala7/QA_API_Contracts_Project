import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_users_response_matches_contract(user_schema):
    response = requests.get(f"{BASE_URL}/users")

    for user in response.json():
        validate(instance=user, schema=user_schema)
