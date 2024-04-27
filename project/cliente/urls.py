from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path("cliente/", views.home, name="home"),
]
