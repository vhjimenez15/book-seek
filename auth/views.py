from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import UserModel
from .serializers import LoginSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LoginView(APIView):

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        operation_description="Login",
        responses={200: openapi.Response(description="access: <token>")},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Username"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Password"
                )
            },
            required=["username", "password"]
        )
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            tokens = serializer.create_token(user)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    @swagger_auto_schema(
        operation_description="User registration",
        responses={200: openapi.Response(description="Create succes")},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Username"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Password"
                ),
                "first_name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="first_name"
                ),
                "last_name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="last_name"
                )
            },
            required=["username", "password", "first_name", "last_name"]
        )
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = make_password(serializer.validated_data["password"])
            extra_fields = {
                "first_name": serializer.validated_data.get("first_name", ""),
                "last_name": serializer.validated_data.get("last_name", ""),
            }
            if UserModel().get_user_by_username(username):
                return Response(
                    {"message": "The user already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = UserModel().create_user(username, password, **extra_fields)
            return Response(
                {"message": "User created.", "id": user},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
