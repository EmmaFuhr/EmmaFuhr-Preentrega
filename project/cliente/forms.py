from django import forms
from . import models
from django.core.exceptions import ValidationError


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "ciudad": forms.TextInput(attrs={"class": "form-control"}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.Pedido
        fields = '__all__'
        widgets = {
            "vendedor": forms.Select(attrs={"class": "form-control"}),
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "articulo": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
            "total_venta": forms.FloatField(),
            "fecha_creacion": forms.HiddenInput(),
            
        }
    def clean(self):
        cleaned_data = super().clean()
        articulo = cleaned_data.get('articulo')
        cantidad = cleaned_data.get('cantidad')

        if articulo and cantidad > articulo.stock:
            raise ValidationError(f"La cantidad solicitada ({cantidad}) excede el stock disponible ({articulo.stock}) del artículo {articulo}.")

        return cleaned_data
