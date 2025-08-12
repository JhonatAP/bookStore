from django.urls import path
from .views import libro_list, LibroCreateView, LibroUpdateView, LibroDeleteView
from . import views

urlpatterns = [
    path('', libro_list, name='lista_libros'),
    path('nuevo/', LibroCreateView.as_view(), name='crear_libro'),
    path('editar/<int:pk>/', LibroUpdateView.as_view(), name='editar_libro'),
    path('eliminar/<int:pk>/', LibroDeleteView.as_view(), name='eliminar_libro'),
    path("registro/", views.register, name="registro"),
]
