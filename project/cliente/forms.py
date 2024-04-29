from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "ciudad": forms.TextInput(attrs={"class": "form-control"}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.Pedido
        fields = '__all__'
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "articulo": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.TextInput(attrs={"class": "form-control"}),
            
        }