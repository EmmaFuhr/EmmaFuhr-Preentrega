from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'core'

urlpatterns = [
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('login/', views.CustomLoginView.as_view(), name ='login'),
    path('register/', views.register, name ='register'),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name ='logout'),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


