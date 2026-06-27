from rest_framework import permissions, status
from rest_framework.views import APIView

from common.responses import success_response
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from .services import AuthService

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = AuthService.register(serializer.validated_data)

        return success_response(
            data={
                "id": str(user.id),
                "email": user.email,
                "username": user.username,
            },
            message="User registered successfully.",
            status_code=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return success_response(
            data={
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            message="Login successful.",
        )
    

class MeAPIView(APIView):

    def get(self, request):

        serializer = UserSerializer(request.user)

        return success_response(
            data=serializer.data,
            message="User profile retrieved successfully.",
        )