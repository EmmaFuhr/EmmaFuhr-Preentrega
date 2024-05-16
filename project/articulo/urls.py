from django.urls import path
from . import views

app_name = 'articulo'

urlpatterns = [
    path("articulo/", views.home, name="home"),
    path("articulo/create/", views.ArticuloCreate.as_view(), name="articulo_create"),
    path("articulo/list/", views.ArticuloList.as_view(), name="articulo_list"),
    path("articulo/detail/<int:pk>", views.ArticuloDetail.as_view(), name="articulo_detail"),
    path("articulo/update/<int:pk>", views.ArticuloUpdate.as_view(), name="articulo_update"),
    path("articulo/delete/<int:pk>", views.ArticuloDelete.as_view(), name="articulo_delete"),

]
