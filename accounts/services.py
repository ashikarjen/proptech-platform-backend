from django.contrib.auth import get_user_model

User = get_user_model()


class AuthService:

    @staticmethod
    def register(validated_data):
        """
        Register a new user.
        """

        return User.objects.create_user(**validated_data)