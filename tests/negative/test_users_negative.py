import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_non_existing_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/999999")

    assert response.status_code == 404
