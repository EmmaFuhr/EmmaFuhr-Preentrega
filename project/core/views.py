from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse



# Create your views here.

def home(request):
    return render (request, 'core/index.html')

def about(request):
    return render (request, 'core/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/login.html",{"mensaje":"Usuario creado correctamente"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
