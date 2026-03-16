from django.shortcuts import redirect

def solo_moderadores(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        if request.user.perfil.rol != "moderador":
            return redirect("/")  # o una página de error

        return view_func(request, *args, **kwargs)
    return wrapper


# Sin usar en hola, pero existe para limitar las acciones a usuarios no moderadores

# {% if user.perfil.rol == "moderador" %} {% endif %} <-- Lineas para ocultar vistas a no moderadores