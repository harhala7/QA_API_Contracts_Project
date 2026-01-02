import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_uses_https():
    assert BASE_URL.startswith("https://")


def test_content_type_is_json():
    response = requests.get(f"{BASE_URL}/users")
    content_type = response.headers.get("Content-Type", "")

    assert response.status_code == 200
    assert "application/json" in content_type


def test_no_sensitive_fields_in_user_response():
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()

    forbidden_fields = {"password", "token", "secret", "creditCard"}

    for user in users:
        for field in forbidden_fields:
            assert field not in user


def test_error_response_does_not_leak_implementation_details():
    response = requests.get(f"{BASE_URL}/users/999999")
    body = response.text.lower()

    assert response.status_code == 404
    assert "exception" not in body
    assert "stack trace" not in body
    assert "traceback" not in body
