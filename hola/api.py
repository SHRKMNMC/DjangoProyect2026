from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Mensaje
from .serializers import MensajeSerializer


# LISTAR y CREAR mensajes
class MensajeListCreateAPI(generics.ListCreateAPIView):
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mensaje.objects.all().order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


# DETALLE: obtener, actualizar, borrar
class MensajeRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]


# MARCAR COMO RESUELTO
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def marcar_resuelto_api(request, pk):
    try:
        mensaje = Mensaje.objects.get(pk=pk)
    except Mensaje.DoesNotExist:
        return Response({"error": "Mensaje no encontrado"}, status=404)

    solucion = request.data.get("solucion", "")

    mensaje.solucion = solucion
    mensaje.resuelto = True
    mensaje.resuelto_por = request.user
    mensaje.save()

    return Response(MensajeSerializer(mensaje).data)
