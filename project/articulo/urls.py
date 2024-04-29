from django.urls import path
from . import views

app_name = 'articulo'

urlpatterns = [
    path("articulo/", views.home, name="home"),
    path("crear_articulo/", views.crear_articulo, name="crear_articulo"),

]
