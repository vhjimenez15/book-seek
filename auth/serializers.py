from .models import UserModel
# from django.contrib.auth import authenticate
from pymongo.errors import PyMongoError
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from config.authentication import jwt_payload_handler
from jwt import encode
from django.conf import settings


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        # Buscar usuario en MongoDB
        try:
            user = UserModel().get_user_by_username(username)
            if user and check_password(password, user["password"]):
                return user
            else:
                raise serializers.ValidationError("Invalid credentials.")
        except PyMongoError as e:
            raise serializers.ValidationError(
                f"Error in db: {str(e)}"
            )

    def create_token(self, user):
        token = encode(
            jwt_payload_handler(user),
            settings.SIMPLE_JWT["SIGNING_KEY"]
        )
        return {"access": token}


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(source='_id', read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
