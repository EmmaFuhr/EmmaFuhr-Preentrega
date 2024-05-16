from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from . import models, forms
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, "articulo/index.html")

class ArticuloList(ListView):
    model = models.Articulo

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(nombre__icontains=consulta) |  
                Q(descripcion__icontains=consulta)  
            )
        return queryset
    
class ArticuloDetail(DetailView):
    model = models.Articulo

class ArticuloDelete(DeleteView):
    model = models.Articulo
    success_url = reverse_lazy("articulo:articulo_list")

class ArticuloCreate(CreateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    success_url = reverse_lazy("articulo:articulo_list")

class ArticuloUpdate(UpdateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    template_name = "articulo/articulo_update.html"
    success_url = reverse_lazy("articulo:articulo_list")






