from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversacion, Mensaje, ConversacionOculta
from .forms import MensajeForm
from django.utils import timezone


@login_required
def lista_conversaciones(request):
    # Todas las conversaciones donde participa el usuario
    conversaciones = (Conversacion.objects.filter(
        usuario1=request.user
    ) | Conversacion.objects.filter(
        usuario2=request.user
    )).exclude(
        id__in=ConversacionOculta.objects.filter(usuario=request.user).values("conversacion_id")
    )

    return render(request, "mensajes/bandeja.html", {
        "conversaciones": conversaciones
    })


@login_required
def chat(request, id):
    conversacion = get_object_or_404(Conversacion, id=id)
    
    # Registrar lectura
    if request.user == conversacion.usuario1:
        conversacion.ultima_lectura_usuario1 = timezone.now()
    else:
        conversacion.ultima_lectura_usuario2 = timezone.now()

    conversacion.save()


    # Seguridad: solo los dos usuarios pueden ver la conversación
    if request.user not in [conversacion.usuario1, conversacion.usuario2]:
        return redirect("lista_conversaciones")

    # Mensajes ordenados cronológicamente
    mensajes = conversacion.mensajes.all().order_by("fecha")

    # Enviar mensaje
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                conversacion=conversacion,
                remitente=request.user,
                contenido=form.cleaned_data["contenido"]
            )
            return redirect("chat", id=id)
    else:
        form = MensajeForm()

    return render(request, "mensajes/chat.html", {
        "conversacion": conversacion,
        "mensajes": mensajes,
        "form": form
    })


@login_required
def borrar_mensaje(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)

    # Solo el remitente puede borrar su mensaje
    if mensaje.remitente == request.user:
        mensaje.delete()

    return redirect("chat", id=mensaje.conversacion.id)

@login_required
def nueva_conversacion(request):
    usuarios = User.objects.exclude(id=request.user.id)

    if request.method == "POST":
        usuario_id = request.POST.get("usuario_id")
        otro = get_object_or_404(User, id=usuario_id)

        # Buscar si ya existe conversación
        conversacion = Conversacion.objects.filter(
            usuario1=request.user, usuario2=otro
        ).first() or Conversacion.objects.filter(
            usuario1=otro, usuario2=request.user
        ).first()

        # Si no existe, crearla
        if not conversacion:
            conversacion = Conversacion.objects.create(
                usuario1=request.user,
                usuario2=otro
            )

        return redirect("chat", id=conversacion.id)

    return render(request, "mensajes/nueva.html", {
        "usuarios": usuarios
    })

@login_required
def borrar_conversacion(request, id):
    conversacion = get_object_or_404(Conversacion, id=id)

    # Seguridad
    if request.user not in [conversacion.usuario1, conversacion.usuario2]:
        return redirect("lista_conversaciones")

    # Marcar como oculta
    ConversacionOculta.objects.get_or_create(
        usuario=request.user,
        conversacion=conversacion
    )

    return redirect("lista_conversaciones")
