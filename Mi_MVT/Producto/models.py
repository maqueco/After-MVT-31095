from pyexpat import model
from django.db import models

# Create your models here.
class Producto(models.Model):

    name = models.CharField(max_length=30)
    price = models.FloatField()
    fecha = models.DateField()
