import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_users_have_non_empty_email():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    for user in users:
        email = user.get("email")
        assert isinstance(email, str)
        assert email.strip() != ""
        assert "@" in email
