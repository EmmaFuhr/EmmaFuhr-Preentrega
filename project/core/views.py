from django.shortcuts import render
from articulo import models

# Create your views here.
def home(request):
    return render (request, 'core/index.html')

