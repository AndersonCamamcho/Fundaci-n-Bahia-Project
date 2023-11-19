from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    identification = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    is_employee = models.BooleanField(default=True)
    is_benefactor = models.BooleanField(default=True)


