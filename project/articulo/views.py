from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView, DetailView, ListView, UpdateView
from . import models, forms
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db import IntegrityError
import logging
# Create your views here.
def home(request):
    return render(request, "articulo/index.html")

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')    
class ArticuloDetail(DetailView):
    model = models.Articulo

logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = models.Articulo
    success_url = reverse_lazy("articulo:articulo_list")
    
    def form_valid(self, form):
        try:
            self.object.delete()
            messages.success(self.request, "Artículo eliminado exitosamente.")
            return redirect(self.success_url)
        except IntegrityError:
            messages.error(self.request, "No se puede eliminar el artículo porque está siendo referenciado por otros registros.")
            return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, "El formulario no es válido.")
        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class ArticuloCreate(CreateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    success_url = reverse_lazy("articulo:articulo_list")

@method_decorator(login_required, name='dispatch')
class ArticuloUpdate(UpdateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    template_name = "articulo/articulo_update.html"
    success_url = reverse_lazy("articulo:articulo_list")






