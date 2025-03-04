from django.db import models

# Create your models here.

class Alumno(models.Model):
    #aqui va los atributos de mi clase
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre