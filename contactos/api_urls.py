# contactos/api_urls.py
from django.urls import path
from .api import ContactoListCreateAPI

urlpatterns = [
    path('', ContactoListCreateAPI.as_view(), name="api_contactos"),
]
