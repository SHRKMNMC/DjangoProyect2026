from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ROLES = (
        ('usuario', 'Usuario normal'),
        ('moderador', 'Moderador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario')

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
