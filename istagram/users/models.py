from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profiles")
