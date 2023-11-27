from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"Servicio: {self.nombre}, Precio: {self.precio}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} es un {self.tipo} de {self.edad} años"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    precio = models.IntegerField()

    def __str__(self):
        return f"Medicamento: {self.nombre}, Precio: {self.precio}"