from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_title = "Articulos"

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")
    list_display_links = ("nombre",)

admin.site.register(models.Articulo, ArticuloAdmin)
