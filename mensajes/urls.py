from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_conversaciones, name='lista_conversaciones'),
    path('nueva/', views.nueva_conversacion, name='nueva_conversacion'),
    path('<int:id>/', views.chat, name='chat'),
    path('borrar/<int:id>/', views.borrar_mensaje, name='borrar_mensaje'),
    path('borrar_conversacion/<int:id>/', views.borrar_conversacion, name='borrar_conversacion'),

]
