from django.db import models

# Create your models here.
class Favorite(models.Model):
  name = models.CharField(max_length=200)
  house = models.CharField(max_length=200)
  blood_status = models.CharField(max_length=200)
  species = models.CharField(max_length=200)
  
