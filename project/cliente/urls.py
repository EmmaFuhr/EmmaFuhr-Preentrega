from django.urls import path
from . import views

app_name = 'cliente'

####### URLs de CLIENTES #######
urlpatterns = [
    path("cliente/", views.home, name="home"),
    path("cliente/create/", views.ClienteCreate.as_view(), name="cliente_create"),
    path("cliente/list/", views.ClienteList.as_view(), name="cliente_list"),
    path("cliente/update/<int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
    path("cliente/delete/<int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),
    path("cliente/detail/<int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    
]

####### URLs de PEDIDOS #######

urlpatterns += [
    path("pedidos/", views.pedidos, name="pedidos"),
    path("pedido/create/", views.PedidoCreate.as_view(), name="pedido_create"),
    path("pedido/list/", views.PedidoList.as_view(), name="pedido_list"),
    path("pedido/update/<int:pk>", views.PedidoUpdate.as_view(), name="pedido_update"),
    path("pedido/delete/<int:pk>", views.PedidoDelete.as_view(), name="pedido_delete"),
    path("pedido/detail/<int:pk>", views.PedidoDetail.as_view(), name="pedido_detail"),

    
]