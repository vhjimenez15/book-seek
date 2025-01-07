from auth.models import UserModel
from datetime import datetime
from django.conf import settings
from django.utils.translation import gettext_lazy
from jwt import decode
from jwt.exceptions import DecodeError, ExpiredSignatureError
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header


class AuthenticationBackend(JWTAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, token):
        model = UserModel()
        try:
            payload = decode(token, settings.SIMPLE_JWT["SIGNING_KEY"])
            user = model.get_one_user(payload["id"])
            if not user:
                return None
            else:
                user.update({"is_authenticated": True})
        except DecodeError:
            msg = gettext_lazy('Token invalid')
            raise exceptions.AuthenticationFailed(msg)
        except ExpiredSignatureError:
            msg = gettext_lazy('Token expired')
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)

    def authenticate(self, request: Request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = gettext_lazy(
                'Invalid token header. No credentials provided.'
            )
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = gettext_lazy(
                'Invalid token header. Token string should not contain spaces.'
            )
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = gettext_lazy('Invalid token header. \
            Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)


def jwt_payload_handler(user: dict):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "exp": datetime.now() + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]
    }
