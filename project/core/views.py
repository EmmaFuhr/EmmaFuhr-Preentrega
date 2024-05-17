from django.shortcuts import render
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView


# Create your views here.
def home(request):
    return render (request, 'core/index.html')

def about(request):
    return render (request, 'core/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


