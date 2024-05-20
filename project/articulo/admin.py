from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_title = "Articulos"

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio","stock", "fecha_actualizacion")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    date_hierarchy = "fecha_actualizacion"

admin.site.register(models.Articulo, ArticuloAdmin)
