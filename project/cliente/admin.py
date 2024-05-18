from django.contrib import admin
from . import models


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "direccion", "ciudad", "fecha_nacimiento")
    list_display_links = ("nombre", "apellido")
    

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente","articulo", "cantidad", "fecha_actualizacion")
    list_display_links = ("cliente",)
    date_hierarchy = "fecha_actualizacion"
    
# Register your models here.
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Pedido, PedidoAdmin)