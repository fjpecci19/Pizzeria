from django.db import models

# Create your models here.


class Pizzas(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    activo = models.BooleanField()

class Ingredientes(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
