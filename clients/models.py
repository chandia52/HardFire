from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    address = models.CharField("Dirección", max_length=75, blank=False, null=False)
    area_number = models.IntegerField("Codigo Postal", blank=False, null=False)
    phone = models.IntegerField("Teléfono", blank=False, null=False)
