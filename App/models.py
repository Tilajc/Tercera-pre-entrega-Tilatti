from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    contrasena = models.CharField(max_length=20)

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    edad = models.IntegerField()

class Medicamento(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()