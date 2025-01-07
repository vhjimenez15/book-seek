from rest_framework.test import APIClient


class CustomAPIClient(APIClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_headers = {}

    def set_auth_token(self, token):
        self.default_headers["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        self.credentials(**self.default_headers)
