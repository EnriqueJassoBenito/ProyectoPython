from django.db import models
from categorias.models import Categoria

# Create your models here.

class Producto(models.Model):
    #aqui va los atributos de mi clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #los campos urlsfields limitan los caracteres a 200 por defecto
    imagen = models .URLField()
    
    # Agregar una relacion con categoria
    # Parametros: 1 )Modelo
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre