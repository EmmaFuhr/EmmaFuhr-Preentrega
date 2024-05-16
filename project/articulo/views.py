from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from . import models, forms
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, "articulo/index.html")

class ArticuloList(ListView):
    model = models.Articulo

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
    success_url = reverse_lazy("articulo:articulo_list")




