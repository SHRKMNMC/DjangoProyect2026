from django.contrib import admin
from django.urls import path, include
from .views import inicio, registro, iniciar_sesion, cerrar_sesion
from rest_framework.authtoken.views import obtain_auth_token #tokens para usuarios

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', inicio, name='inicio'),

    path('login/', iniciar_sesion, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', cerrar_sesion, name='logout'),

    path('hola/', include('hola.urls')),
    path('bot/', include('bot.urls')),

    path("contactos/", include("contactos.urls")),
    path("api/contactos/", include("contactos.api_urls")), #Contactos API End-point 

    path("datos/", include("datos.urls")),

    path('mensajes/', include('mensajes.urls')),
    path('cuentas/', include('cuentas.urls')),
    
    path('api/login/', obtain_auth_token), #Tokens para los usuarios
    
    path('api/hola/', include('hola.api_urls')), #Alertas API End-point



]

