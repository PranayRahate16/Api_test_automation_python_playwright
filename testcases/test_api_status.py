import pytest
from api_clients.status_api import StatusAPI


class Test_API_Status:
    ENDPOINT='/status'

    def test_api_status(self, api_request_context):
        status=StatusAPI(api_request_context)
        response=status.get_api_status()
        assert response.status == 200
        jsondata=response.json()
        print(jsondata.get('status'))


