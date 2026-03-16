from rest_framework import serializers
from .models import Mensaje

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'
        read_only_fields = ['id', 'fecha', 'creado_por', 'resuelto_por']
