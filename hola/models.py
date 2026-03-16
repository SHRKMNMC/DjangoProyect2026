from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    texto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    solucion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)

    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mensajes_creados_alertas"
    )

    resuelto_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mensajes_resueltos_alertas"
    )

    def __str__(self):
        return self.texto
