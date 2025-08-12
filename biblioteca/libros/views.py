from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Libro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

@login_required
def libro_list(request):
    query = request.GET.get('q', '')  # Búsqueda
    #libros = Libro.objects.all()
    if request.user.is_superuser:
        libros = Libro.objects.all()
    else:
        libros = Libro.objects.filter(usuario=request.user)

    if query:
        libros = libros.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query) | Q(isbn__icontains=query)
        )

    # Paginación
    paginator = Paginator(libros, 5)  # 5 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'libros/lista.html', {
        'page_obj': page_obj,
        'query': query
    })

def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        
        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            usuario=request.user  # ← aquí asociamos el usuario
        )
        return redirect('lista_libros')
    
    return render(request, 'agregar_libro.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Cuenta creada para {username}. ¡Ahora puedes iniciar sesión!")
            
            # Inicia sesión automáticamente después de registrarse
            login(request, user)
            return redirect("/")  # Cambia 'inicio' por la URL de tu página principal
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'libros/formulario.html'
    fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
    success_url = reverse_lazy('lista_libros')

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = 'libros/formulario.html'
    fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
    success_url = reverse_lazy('lista_libros')

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'libros/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_libros')
