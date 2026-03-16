from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('editar/<int:id>/', views.editar_mensaje, name='editar_mensaje'),
    path('borrar/<int:id>/', views.borrar_mensaje, name='borrar_mensaje'),

    path('resuelto/<int:id>/', views.marcar_resuelto, name='marcar_resuelto'),

]
