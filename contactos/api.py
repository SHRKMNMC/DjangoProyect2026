from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Contacto
from .serializers import ContactoSerializer

class ContactoListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contacto.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
