from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path("cliente/", views.home, name="home"),
    path("cliente/create/", views.ClienteCreate.as_view(), name="cliente_create"),
    path("cliente/list/", views.ClienteList.as_view(), name="cliente_list"),
    path("cliente/update/<int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),
    path("cliente/detail/<int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("crear_pedidos/", views.crear_pedido, name="crear_pedidos"),

]
