# API Test Automation — Simple Grocery Store API

This project automates the API tests for the [Simple Grocery Store API](https://simple-grocery-store-api.glitch.me) using Python, pytest, and Playwright's API request fixtures.

## Tech Stack

- Python 3.x
- Pytest
- Playwright
- Allure
- Faker
- Jenkins pipeline support

## Project Structure

```text
requestsModule_python/
├── .gitignore
├── Jenkinsfile
├── pytest.ini
├── README.md
├── requirements.txt
├── allure-report/           # generated report output
├── allure-results/           # raw results for Allure
├── api_clients/              # API wrapper classes for each endpoint
│   ├── Create_Cart_api.py    # cart creation and cart-item operations
│   ├── client_api.py         # client registration / access token flow
│   ├── product_api.py        # product lookup endpoints
│   ├── status_api.py         # API status endpoint
│   └── __pycache__/
├── config/
│   ├── __init__.py
│   └── config.py            # base URL configuration
├── reports/                 # pytest HTML report output
├── SimpleGroceryStore/      # project folder present in workspace
├── testcases/
│   ├── __init__.py
│   ├── api_tests/
│   │   ├── __init__.py
│   │   ├── conftest.py      # shared Playwright request fixtures
│   │   ├── Test_api_client_authorization.py
│   │   ├── Test_create_cart_api.py
│   │   ├── Test_get_all_products.py
│   │   └── test_api_status.py
│   └── smoke/
│       ├── __init__.py
│       ├── conftest.py
│       └── test_smoke_flow.py
└── .venv/                   # local virtual environment
```

## Key Files

- `pytest.ini` configures test discovery, HTML report generation, and Allure output.
- `config/config.py` stores the API base URL.
- `testcases/api_tests/conftest.py` creates shared fixtures such as `api_request_context`, `access_token`, and `cart_id`.
- `testcases/smoke/test_smoke_flow.py` validates a full happy-path purchase flow.
- `Jenkinsfile` runs the suite with a smoke/regression selection parameter.

## Setup

```bash
cd requestsModule_python
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Windows cmd
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install --with-deps
```

## Run Tests

```bash
# Run the full suite
pytest

# Run only smoke tests
pytest -m smoke

# Run only API tests
pytest -m api

# Run a specific test file
pytest testcases/api_tests/test_api_status.py -v

# Run a specific smoke scenario
pytest testcases/smoke/test_smoke_flow.py -v -s
```

## Reports

The project is configured to generate both HTML and Allure outputs:

- Pytest HTML report: `reports/report.html`
- Allure results: `allure-results/`
- Allure HTML report: `allure-report/`

## Test Design

The suite is organized around endpoint-level API wrappers and reusable fixtures:

- `api_clients/` contains classes that encapsulate each API resource.
- `testcases/api_tests/` holds isolated endpoint tests.
- `testcases/smoke/` contains end-to-end flow validation.
- Fixtures create new client tokens and cart state per session so tests remain independent.

## Jenkins

The `Jenkinsfile` supports a parameterized pipeline with these options:

- `all`
- `smoke`
- `regression`

It creates a virtual environment, installs dependencies, executes pytest, and publishes HTML/Allure results.

## Notes

- `ClientAPI.register_client()` returns the access token used by authenticated flows.
- `CreateCartAPI` covers cart creation and item addition.
- `ProductAPI` covers product listing and filtering operations.
- `StatusAPI` validates the API health check endpoint.

## THANKS
