# API Test Automation — Python + Playwright

API test automation framework for the [Simple Grocery Store API](https://simple-grocery-store-api.glitch.me), built with Python, Playwright's API request context, and pytest.

## Tech Stack

- **Python 3.13**
- **Playwright** — API request context (`playwright.request`)
- **pytest** — test runner
- **pytest-html** — HTML test reports
- **Faker** — test data generation

## Project Structure

```
requestsModule_python/
│
├── api_clients/              # API client layer — one class per resource
│   ├── client_api.py         # /api-clients — client registration
│   ├── cart_api.py           # /carts — cart creation & item management
│   └── product_api.py        # /products — product lookups
│
├── config/
│   └── config.py             # BASE_URL and environment config
│
├── testcases/
│   ├── conftest.py           # shared fixtures: api_request_context, access_token, cart_id
│   ├── test_client_authorization.py
│   ├── test_cart.py
│   ├── test_get_all_products.py
│   ├── test_get_req.py
│   └── test_smoke_flow.py    # end-to-end smoke test (status -> products -> auth -> cart -> item)
│
├── reports/                  # generated HTML test reports (git-ignored)
├── pytest.ini                 # test discovery config & default CLI options
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/PranayRahate16/Api_test_automation_python_playwright.git
cd Api_test_automation_python_playwright

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
# Run everything
pytest

# Run only smoke tests
pytest -m smoke

# Run a specific file
pytest testcases/test_cart.py -v -s
```

HTML report is generated at `reports/report.html` after each run.

## Fixtures (conftest.py)

| Fixture | Scope | Provides |
|---|---|---|
| `api_request_context` | function | Playwright request context bound to `BASE_URL` |
| `access_token` | function | Registers a new client and returns an `accessToken` |
| `cart_id` | function | Creates a new cart using `access_token` and returns its `cartId` |

Each fixture builds fresh state per test, so tests remain independent and safe to run in any order or in parallel.

## Design Notes

- **API client layer** (`api_clients/`) mirrors the Page Object Model used for UI automation — each class wraps one resource's endpoints, keeping payload shape and headers in one place.
- **Tests stay thin** — they call client methods and assert on responses; they don't build requests directly.
- **`test_smoke_flow.py`** is a separate end-to-end test that replays the real user journey in sequence, distinct from the isolated per-endpoint tests.
