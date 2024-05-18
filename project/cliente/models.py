from django.db import models
from articulo.models import Articulo
from django.utils import timezone

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    dni = models.CharField(max_length=8,verbose_name='DNI', unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    direccion =  models.CharField(max_length=200, verbose_name='Dirección')
    ciudad =  models.CharField(max_length=200, verbose_name='Ciudad', default='',null=False)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = 'Cliente'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Cliente')
    articulo = models.ForeignKey(Articulo,on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Artículo')
    cantidad = models.IntegerField(verbose_name='Cantidad', default=0)
    fecha_actualizacion = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return f"{self.cliente} - Art.: {self.articulo} Cantidad: {self.cantidad} "