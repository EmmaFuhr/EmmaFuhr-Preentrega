from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path("cliente/", views.home, name="home"),
    path("crear_cliente/", views.crear_cliente, name="crear_cliente"),
]
