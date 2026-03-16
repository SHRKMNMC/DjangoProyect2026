from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .decorators import solo_moderadores

@solo_moderadores
def panel_usuarios(request):
    usuarios = User.objects.all().select_related("perfil")
    return render(request, "cuentas/panel.html", {"usuarios": usuarios})

@solo_moderadores
def cambiar_rol(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    # Si el usuario NO tiene perfil, lo creamos
    if not hasattr(usuario, "perfil"):
        from cuentas.models import Perfil
        Perfil.objects.create(user=usuario, rol="usuario")

    # Alternar rol
    if usuario.perfil.rol == "usuario":
        usuario.perfil.rol = "moderador"
    else:
        usuario.perfil.rol = "usuario"

    usuario.perfil.save()
    return redirect("panel_usuarios")

@solo_moderadores
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    # Evitar que un moderador se elimine a sí mismo
    if usuario == request.user:
        return redirect("panel_usuarios")

    # Si tiene perfil, lo borramos primero
    if hasattr(usuario, "perfil"):
        usuario.perfil.delete()

    # Luego borramos el usuario
    usuario.delete()

    return redirect("panel_usuarios")
