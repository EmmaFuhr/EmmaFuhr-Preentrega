from django.db import models
from django.utils import timezone

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')
    precio =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Precio')
    stock = models.PositiveIntegerField(verbose_name='Stock', default=0)
    fecha_actualizacion = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de actualización")
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Artículos"
        verbose_name = 'Artículo'