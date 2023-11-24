from django.db import models
from user_carpeta.models import CustomUser


class Beneficiary(models.Model):

    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    identification = models.CharField(max_length=9)
    birthdate = models.DateField(verbose_name='Birthday')
    registration_date = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='records')
