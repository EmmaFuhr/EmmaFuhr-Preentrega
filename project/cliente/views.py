from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def home(request):
    consulta= request.GET.get("consulta", None)
    if consulta:
        consulta_clientes=models.Cliente.objects.filter(nombre__icontains=consulta)
        if consulta_clientes.count() == 0: #si no encuentra al cliente por nombre lo busca por apellido
            consulta_clientes=models.Cliente.objects.filter(apellido__icontains=consulta)
    else:
        consulta_clientes = consulta_clientes = models.Cliente.objects.all()
    context = {"clientes": consulta_clientes}
    return render(request, "cliente/index.html", context)


def crear_cliente(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:home')
    else:
        form = forms.ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})


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