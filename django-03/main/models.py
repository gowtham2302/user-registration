from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NewUser(AbstractUser):
    api_key = models.CharField(max_length=100 , null=True , blank=True)
    Doctor_attending = models.CharField(max_length=100 , null=True , blank=True)
    date_of_visit=models.DateField(null=True , blank=True)
    last_date_of_visit=models.DateField(null=True , blank=True)