from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def home(request):
    consulta_clientes = models.Cliente.objects.all()
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