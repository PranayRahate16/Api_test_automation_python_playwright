from config import config


class ClientAPI:
    """Encapsulates all /api_clients endpoint interactions."""

    ENDPOINT = "/api-clients"

    def __init__(self, request_context):
        self.request_context = request_context

    def register_client(self, name: str, email: str):
        payload = {
             "clientName": name,
            "clientEmail": email
        }
        return self.request_context.post(
            self.ENDPOINT,
            data=payload
        )