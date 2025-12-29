import json
import pytest


@pytest.fixture
def user_schema():
    with open("schemas/user_schema.json") as f:
        return json.load(f)
