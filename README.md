[![API Tests](https://github.com/harhala7/QA_API_Contracts_Project/actions/workflows/tests.yml/badge.svg)](https://github.com/harhala7/QA_API_Contracts_Project/actions/workflows/tests.yml)

## What this project demonstrates
- API testing using pytest and requests
- Contract testing to validate API schemas and responses
- Positive and negative test scenarios
- Basic security hygiene (headers, auth assumptions)
- Clean, scalable test structure

## Tech stack
- Python
- Pytest
- Requests

## How to run
```bash
pip install -r requirements.txt
pytest 
```

## Project structure
```text
tests/
  test_users_happy.py
  contracts/
    test_users_contract.py
  negative/
    test_users_negative.py
schemas/
  user_schema.json
```


## Target API
Public test API used for demonstration purposes:

https://jsonplaceholder.typicode.com  
GET /users


## Security hygiene checks

This project includes basic API security hygiene tests commonly performed by QA Engineers:

- HTTPS usage verification
- Response `Content-Type` validation (`application/json`)
- Detection of sensitive data exposure in API responses (e.g. passwords, tokens)
- Validation that error responses do not leak implementation details (stack traces, exceptions)

These checks help identify common security and data exposure risks early, without performing penetration testing.
