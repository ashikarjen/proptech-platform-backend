from rest_framework import permissions, status
from rest_framework.views import APIView

from common.responses import success_response
from .serializers import RegisterSerializer
from .services import AuthService


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