from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """
    Model to store users
    """
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username