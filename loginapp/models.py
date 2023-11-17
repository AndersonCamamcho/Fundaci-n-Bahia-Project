from django.db import models


class Beneficiarios(models.Model):
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Identification =models.CharField(max_length=9)
    birthdate= models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    image =
