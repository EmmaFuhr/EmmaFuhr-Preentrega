from django.contrib import admin
from . import models


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "direccion", "ciudad", "fecha_nacimiento", "avatar")
    list_display_links = ("nombre", "apellido")
    

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("vendedor","cliente","articulo", "cantidad", "total_venta", "fecha_creacion")
    list_display_links = ("cliente",)
    search_fields = ("cliente__nombre","cliente__apellido", "articulo__nombre", "vendedor__nombre__username")
    date_hierarchy = "fecha_creacion"

    
  
    
# Register your models here.
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Pedido, PedidoAdmin)