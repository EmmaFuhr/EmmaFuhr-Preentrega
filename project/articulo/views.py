from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    consulta_articulos = models.Articulo.objects.all()
    context = {"articulos": consulta_articulos}
    return render(request, "articulo/index.html", context)