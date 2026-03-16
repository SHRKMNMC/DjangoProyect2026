from django.urls import path
from .api import (
    MensajeListCreateAPI,
    MensajeRetrieveUpdateDeleteAPI,
    marcar_resuelto_api
)

urlpatterns = [
    path('', MensajeListCreateAPI.as_view(), name='api_mensajes'),
    path('<int:pk>/', MensajeRetrieveUpdateDeleteAPI.as_view(), name='api_mensaje_detalle'),
    path('<int:pk>/resolver/', marcar_resuelto_api, name='api_mensaje_resolver'),
]
