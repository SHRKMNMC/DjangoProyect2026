from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required

@login_required
def saludo(request):

    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.creado_por = request.user
            form.save()
            return redirect('/hola/')
    else:
        form = MensajeForm()

    mensajes = Mensaje.objects.all().order_by('-fecha')

    return render(request, "hola/saludo.html", {
        "form": form,
        "mensajes": mensajes
    })


@login_required
def editar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)

    if request.method == "POST":
        form = MensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect('/hola/')
    else:
        form = MensajeForm(instance=mensaje)

    return render(request, "hola/editar.html", {"form": form})



@login_required 
def borrar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    return redirect('/hola/')


@login_required
def marcar_resuelto(request, id):
    mensaje = Mensaje.objects.get(id=id)

    if request.method == "POST":
        solucion = request.POST.get("solucion")
        mensaje.solucion = solucion
        mensaje.resuelto = True
        mensaje.resuelto_por = request.user
        mensaje.save()
        return redirect('/hola/')

    return render(request, "hola/resolver.html", {"mensaje": mensaje})

