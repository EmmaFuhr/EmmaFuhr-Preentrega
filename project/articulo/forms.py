from django import forms
from . import models

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = models.Articulo
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
        }