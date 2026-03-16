from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_contactos, name="lista_contactos"),
    path("borrar/<int:id>/", views.borrar_contacto, name="borrar_contacto"),
    path("editar/<int:id>/", views.editar_contacto, name="editar_contacto"),
]
