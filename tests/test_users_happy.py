import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_returns_200_and_list():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
