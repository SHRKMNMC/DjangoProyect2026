from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mensajes.models import Conversacion, Mensaje, ConversacionOculta


@login_required
def inicio(request):

    conversaciones = (Conversacion.objects.filter(usuario1=request.user) |
                      Conversacion.objects.filter(usuario2=request.user))

    conversaciones_visibles = conversaciones.exclude(
        id__in=ConversacionOculta.objects.filter(usuario=request.user).values("conversacion_id")
    )

    hay_mensajes_nuevos = False

    for conv in conversaciones_visibles:

        # Última lectura según el usuario
        ultima_lectura = (
            conv.ultima_lectura_usuario1
            if conv.usuario1 == request.user
            else conv.ultima_lectura_usuario2
        )

        # Caso 1: nunca ha abierto la conversación → todos los mensajes recibidos son nuevos
        if ultima_lectura is None:
            nuevos = conv.mensajes.exclude(remitente=request.user)
        else:
            # Caso 2: comparar fechas
            nuevos = conv.mensajes.filter(
                fecha__gt=ultima_lectura
            ).exclude(remitente=request.user)

        if nuevos.exists():
            hay_mensajes_nuevos = True
            break

    return render(request, "inicio.html", {
        "hay_mensajes_nuevos": hay_mensajes_nuevos
    })






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
