from django.db import models
from articulo.models import Articulo

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    dni = models.CharField(max_length=8,verbose_name='DNI', unique=True)
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
    
    def __str__(self):
        return f"{self.cliente} - Art.: {self.articulo} Cantidad: {self.cantidad} "