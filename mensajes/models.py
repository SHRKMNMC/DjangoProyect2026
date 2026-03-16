from django.db import models
from django.contrib.auth.models import User

class Conversacion(models.Model):
    usuario1 = models.ForeignKey(User, related_name="conversaciones1", on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(User, related_name="conversaciones2", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario1.username} ↔ {self.usuario2.username}"

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name="mensajes", on_delete=models.CASCADE)
    remitente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mensajes_enviados_chat"
    )
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remitente.username}: {self.contenido[:20]}"

class ConversacionOculta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'conversacion')
