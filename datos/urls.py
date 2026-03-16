from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_datos, name='cargar_datos'),
    path('borrar/<int:id>/', views.borrar_tabla, name='borrar_tabla'),
    path('ver/<int:id>/', views.ver_tabla, name='ver_tabla'),
    path('resumen/', views.resumen_usuarios, name='resumen_usuarios'),
]
