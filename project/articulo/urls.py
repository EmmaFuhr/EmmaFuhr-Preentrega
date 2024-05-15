from django.urls import path
from . import views

app_name = 'articulo'

urlpatterns = [
    path("articulo/", views.home, name="home"),
    path("articulo/create/", views.articulo_create, name="articulo_create"),
    path("articulo/list/", views.articulo_list, name="articulo_list"),

]
