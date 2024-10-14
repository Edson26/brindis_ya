from django.db import models

# Create your models here.


class Trabajador(models.Model):
    nombre = models.CharField(max_length=30)
    HOMBRE = "Hombre"
    MUJER = "Mujer"
    GENERO = [
        (HOMBRE, "Hombre"),
        (MUJER, "Mujer")
    ]
    sexo = models.CharField(max_length=6, choices=GENERO, default=HOMBRE)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=30)

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()

class Receta(models.Model):
    nombre = models.CharField(max_length=30)

class Coctel(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    ingrediente = models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.CASCADE)
    