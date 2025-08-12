from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libros.urls')),
    path('base/', base_view, name='base'),  # nombre 'base'
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("registro/", views.register, name="registro"),
]
