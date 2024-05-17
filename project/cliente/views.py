from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, "cliente/index.html")

def pedidos(request):
    return render(request, "cliente/pedidos.html")

   
######### CLASES DE CLIENTES #########

class ClienteList(ListView):
    model = models.Cliente

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(nombre__icontains=consulta) |  
                Q(apellido__icontains=consulta)  
            )
        return queryset
    
class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")

class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")

class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    template_name = "cliente/cliente_update.html"
    success_url = reverse_lazy("cliente:cliente_list")

######### CLASES DE PEDIDOS #########

class PedidoList(ListView):
    model = models.Pedido
    

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(cliente__nombre__icontains=consulta) |
                Q(cliente__apellido__icontains=consulta) |  
                Q(articulo__nombre__icontains=consulta)                 
            )
        return queryset
    
class PedidoDetail(DetailView):
    model = models.Pedido

class PedidoDelete(DeleteView):
    model = models.Pedido
    success_url = reverse_lazy("cliente:pedido_list")

class PedidoCreate(CreateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    success_url = reverse_lazy("cliente:pedido_list")

class PedidoUpdate(UpdateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    template_name = "cliente/pedido_update.html"
    success_url = reverse_lazy("cliente:pedido_list")