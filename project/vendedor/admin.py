from django.contrib import admin
from . import models


class VendedorAdmin(admin.ModelAdmin):
    list_display = ("nombre","telefono", "ciudad", "fecha_alta", "avatar")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_alta"
    

admin.site.register(models.Vendedor, VendedorAdmin)