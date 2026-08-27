


class StatusAPI:
    def __init__(self,request_context):
        self.request_context=request_context

    ENDPOINT='/status'

    def get_api_status(self):
        return self.request_context.get(self.ENDPOINT)
