from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Vendedor(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    ciudad =  models.CharField(max_length=200, verbose_name='Ciudad')
    fecha_alta = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de Alta")
    avatar = models.ImageField(upload_to="avatares", null= True, blank=True)

    def __str__(self):
        return self.nombre.username
    
    class Meta:
        verbose_name_plural = "Vendedores"
        verbose_name = 'Vendedor'


