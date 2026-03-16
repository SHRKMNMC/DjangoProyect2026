from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('borrar/', views.borrar_chat, name='borrar_chat'),

]
