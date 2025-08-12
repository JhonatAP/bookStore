from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def base_view(request):
    return render(request, "libros/lista.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Usuario {username} registrado con éxito")
            login(request, user)  # Inicia sesión automáticamente tras registrarse
            return redirect("/")  # Cambia 'inicio' por el nombre de tu vista principal
        else:
            messages.error(request, "Por favor corrige los errores en el formulario")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # Cambia por tu página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")  # Usa tu propia plantilla

def custom_logout(request):
    logout(request)
    return redirect("base")  # Redirige al login
