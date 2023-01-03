from django.db import models

class Familiares(models.Model):
    tipo_de_familiar = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    mayor_de_edad = models.BooleanField()
    