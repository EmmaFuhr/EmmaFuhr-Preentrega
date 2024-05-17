from django.contrib import admin
from . import models


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "direccion", "ciudad")
    list_display_links = ("nombre", "apellido")

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente","articulo", "cantidad")
    list_display_links = ("cliente",)

# Register your models here.
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Pedido, PedidoAdmin)