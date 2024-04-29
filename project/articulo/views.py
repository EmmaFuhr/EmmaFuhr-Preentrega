from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.
def home(request):
    consulta_articulos = models.Articulo.objects.all()
    context = {"articulos": consulta_articulos}
    return render(request, "articulo/index.html", context)

def crear_articulo(request):
    if request.method == "POST":
        form = forms.ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulo:home')
    else:
        form = forms.ArticuloForm()
    return render(request, 'articulo/crear_articulo.html', {'form': form})