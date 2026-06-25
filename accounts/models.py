from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True,
    )

    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email