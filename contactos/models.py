from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

class Contacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    telefono = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(9, "El teléfono debe tener al menos 9 caracteres."),
            RegexValidator(
                r'^[0-9+\-\s]+$',
                "Solo se permiten números, espacios, + y -"
            )
        ]
    )

    email = models.EmailField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
