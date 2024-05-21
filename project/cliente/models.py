from django.db import models, transaction
from articulo.models import Articulo
from django.utils import timezone
from vendedor.models import Vendedor
from django.db.models import F
from django.core.exceptions import ValidationError

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    dni = models.CharField(max_length=8,verbose_name='DNI', unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    direccion =  models.CharField(max_length=200, verbose_name='Dirección')
    ciudad =  models.CharField(max_length=200, verbose_name='Ciudad', default='',null=False)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = 'Cliente'

class Pedido(models.Model):
    vendedor = models.ForeignKey(Vendedor,on_delete=models.DO_NOTHING, verbose_name="Vendedor")
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Cliente')
    articulo = models.ForeignKey(Articulo,on_delete=models.DO_NOTHING,verbose_name='Artículo')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad', default=0)
    total_venta = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total venta', editable=False)
    fecha_creacion = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de creación")
    
    def __str__(self):
        return f"{self.cliente} - Art.: {self.articulo} Cantidad: {self.cantidad} "
    
    class Meta:
        ordering = ("-fecha_creacion",)
    
    #def clean(self):
    #    if self.articulo and self.cantidad > self.articulo.stock:
    #        raise ValidationError(f"La cantidad solicitada ({self.cantidad}) excede el stock disponible ({self.articulo.stock}) del artículo {self.articulo}.")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk:
                pedido_anterior = Pedido.objects.select_for_update().get(pk=self.pk)
                cantidad_anterior = pedido_anterior.cantidad
                articulo_anterior = pedido_anterior.articulo
            else:
                cantidad_anterior = 0
                articulo_anterior = None

            if articulo_anterior and articulo_anterior != self.articulo:
                # Reponer el stock del artículo anterior si el artículo ha cambiado
                articulo_anterior.stock += cantidad_anterior
                articulo_anterior.save()

            # Verificar el stock disponible del artículo actual
            stock_disponible = self.articulo.stock
            if self.pk:
                stock_disponible += cantidad_anterior

            if self.cantidad > stock_disponible:
                raise ValidationError(f"La cantidad solicitada ({self.cantidad}) excede el stock disponible ({stock_disponible}) del artículo {self.articulo}.")

            # Actualizar el stock del artículo actual
            self.articulo.stock = stock_disponible - self.cantidad
            self.articulo.save()

            # Calcular el total de la venta
            self.total_venta = self.articulo.precio * self.cantidad

            # Guardar el pedido
            super().save(*args, **kwargs)