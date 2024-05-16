from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, "cliente/index.html")

'''
def crear_cliente(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:home')
    else:
        form = forms.ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

'''
def pedidos(request):
    consulta= request.GET.get("consulta", None)
    if consulta:
        consulta_pedidos=models.Pedido.objects.filter(cliente__nombre__icontains=consulta)
        if consulta_pedidos.count() == 0: #si no encuentra al cliente por nombre lo busca por apellido
            consulta_pedidos=models.Pedido.objects.filter(cliente__apellido__icontains=consulta)
    else:
        consulta_pedidos = consulta_pedidos = models.Pedido.objects.all()
    context = {"pedidos": consulta_pedidos}
    return render(request, "cliente/pedidos.html", context)


def crear_pedido(request):
    if request.method == "POST":
        form = forms.PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:pedidos')
    else:
        form = forms.PedidoForm()
    return render(request, 'cliente/crear_pedido.html', {'form': form})
   
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