from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    address = models.CharField("Dirección", max_length=75, blank=False, null=True)
    area_number = models.IntegerField("Codigo Postal", blank=False, null=True)
    phone = models.IntegerField("Teléfono", blank=False, null=True)
