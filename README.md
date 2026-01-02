[![API Tests](https://github.com/harhala7/QA_API_Contracts_Project/actions/workflows/tests.yml/badge.svg)](https://github.com/harhala7/QA_API_Contracts_Project/actions/workflows/tests.yml)

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

## Security hygiene checks

This project includes basic API security hygiene tests commonly performed by QA Engineers:

- HTTPS usage verification
- Response `Content-Type` validation (`application/json`)
- Detection of sensitive data exposure in API responses (e.g. passwords, tokens)
- Validation that error responses do not leak implementation details (stack traces, exceptions)

These checks help identify common security and data exposure risks early, without performing penetration testing.
