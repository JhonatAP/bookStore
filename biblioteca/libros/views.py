from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Libro

# Create your views here.


class LibroListView(ListView):
    model = Libro
    template_name = 'libros/lista.html'

class LibroCreateView(CreateView):
    model = Libro
    template_name = 'libros/formulario.html'
    fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
    success_url = reverse_lazy('lista_libros')

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'libros/formulario.html'
    fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
    success_url = reverse_lazy('lista_libros')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_libros')