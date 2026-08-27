import faker
from api_clients.client_api import ClientAPI

fake = faker.Faker()


class TestClientAuthorization:

    def test_client_registration_returns_access_token(self, api_request_context):
        client_api = ClientAPI(api_request_context)

        response = client_api.register_client(
            name=fake.name(),
            email=fake.safe_email()
        )

        assert response.status == 201, (
            f"Expected 201, got {response.status}. Body: {response.text()}"
        )

        response_data = response.json()
        assert "accessToken" in response_data, f"No accessToken in response: {response_data}"

        access_token = response_data["accessToken"]
        print(f"Access token: {access_token}")