from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class UserListings(models.Model):

    Nombre = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Nombre}"