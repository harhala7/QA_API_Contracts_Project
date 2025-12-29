# API Contract Testing (Python)

API-only QA project using **pytest**, **requests** and **jsonschema** to validate API responses against a contract (schema).

## What is covered
- Happy path API tests
- Negative tests (error handling)
- Contract tests using JSON Schema validation

## Project structure
tests/
  test_users_happy.py
  contracts/
    test_users_contract.py
  negative/
    test_users_negative.py
schemas/
   user_schema.json

   
## Run locally
```bash
pip install -r requirements.txt
pytest

## Target API

https://jsonplaceholder.typicode.com

GET /users