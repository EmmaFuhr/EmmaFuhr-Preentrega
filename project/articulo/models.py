from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
    precio =  models.CharField(max_length=200, verbose_name='Precio')

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name_plural = "Artículos"
        verbose_name = 'Artículo'