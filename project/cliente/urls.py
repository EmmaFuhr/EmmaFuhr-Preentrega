from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path("home/", views.home, name="home"),
]
