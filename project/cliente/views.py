from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "cliente/index.html")

@login_required
def pedidos(request):
    return render(request, "cliente/pedidos.html")

   
######### CLASES DE CLIENTES #########
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class ClienteDetail(DetailView):
    model = models.Cliente

@method_decorator(login_required, name='dispatch')
class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")


@method_decorator(login_required, name='dispatch')
class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    template_name = "cliente/cliente_update.html"
    success_url = reverse_lazy("cliente:cliente_list")

######### CLASES DE PEDIDOS #########
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')   
class PedidoDetail(DetailView):
    model = models.Pedido

@method_decorator(login_required, name='dispatch')
class PedidoDelete(LoginRequiredMixin,DeleteView):
    model = models.Pedido
    success_url = reverse_lazy("cliente:pedido_list")
    
@method_decorator(login_required, name='dispatch')
class PedidoCreate(CreateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    success_url = reverse_lazy("cliente:pedido_list")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

@method_decorator(login_required, name='dispatch')
class PedidoUpdate(UpdateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    template_name = "cliente/pedido_update.html"
    success_url = reverse_lazy("cliente:pedido_list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            error_message = str(e)
            form.add_error(None, error_message)  
            return self.form_invalid(form)

