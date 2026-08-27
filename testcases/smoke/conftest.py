import os
import subprocess

import pytest

from api_clients.Create_Cart_api import CreateCartAPI
from api_clients.client_api import ClientAPI
from config import config
from testcases.api_tests.Test_api_client_authorization import fake


@pytest.fixture (scope='session')
def api_request_context(playwright):
    context = playwright.request.new_context(base_url=config.Config.BASE_URL)
    yield context
    context.dispose()

@pytest.fixture (scope='session')
def access_token(api_request_context):
    client_api = ClientAPI(api_request_context)
    response = client_api.register_client(
        name=fake.name(),
        email=fake.safe_email()
    )
    assert response.status == 201, f"Failed to register client: {response.text()}"
    return response.json()['accessToken']


@pytest.fixture (scope='session')
def cart_id(api_request_context,access_token):
    cart_api=CreateCartAPI(api_request_context)
    response=cart_api.create_cart(access_token)
    assert response.status == 201, f"Failed to create cart: {response.text()}"
    return response.json()['cartId']


def pytest_sessionfinish(session, exitstatus):
    """Generate an Allure report without blocking the test run."""
    if hasattr(session.config, "workerinput"):
        return

    print("\n--- Test session completed. Generating Allure report... ---")

    results_dir = "allure-results"
    output_dir = "allure-report"

    if os.path.exists(results_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            result = subprocess.run(
                ["allure", "generate", results_dir, "-o", output_dir, "--clean"],
                check=False,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print(f"Allure report generated at {output_dir}")
            else:
                print(f"Allure generation failed:\n{result.stderr}")
        except Exception as e:
            print(f"Could not generate Allure report via CLI: {e}")
