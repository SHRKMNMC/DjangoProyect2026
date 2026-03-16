from django.urls import path
from . import views

urlpatterns = [
    path("", views.panel_usuarios, name="panel_usuarios"),
    path("cambiar-rol/<int:user_id>/", views.cambiar_rol, name="cambiar_rol"),
    path("eliminar/<int:user_id>/", views.eliminar_usuario, name="eliminar_usuario"),

]
