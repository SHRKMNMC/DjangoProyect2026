from django.db import models

class MensajeBot(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=20, default="usuario")  # usuario o bot

    def __str__(self):
        return f"{self.autor}: {self.texto}"
