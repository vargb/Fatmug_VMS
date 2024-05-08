from django.db import models
from rest_framework_simplejwt.models import TokenUser
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(TokenUser):
    middle_name=models.CharField(max_length=255)
