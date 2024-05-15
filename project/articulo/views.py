from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from . import models, forms
# Create your views here.
def home(request):
    return render(request, "articulo/index.html")

def articulo_list(request):
    consulta= request.GET.get("consulta", None)
    if consulta:
        consulta_articulos=models.Articulo.objects.filter(nombre__icontains=consulta)
    else:
        consulta_articulos= models.Articulo.objects.all()
    context = {"articulos": consulta_articulos}
    return render(request, "articulo/articulo_list.html", context)


def articulo_create(request):
    if request.method == "POST":
        form = forms.ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulo:home')
    else:
        form = forms.ArticuloForm()
    return render(request, 'articulo/articulo_create.html', {'form': form})