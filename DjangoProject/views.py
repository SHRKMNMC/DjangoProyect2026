from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


@login_required
def inicio(request):
    return render(request, "inicio.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {"error": "Credenciales incorrectas"})

    return render(request, "login.html")


def cerrar_sesion(request):
    logout(request)
    return redirect('/login/')


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('/')
    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})
