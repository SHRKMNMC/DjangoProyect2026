from django.db import models

class TablaGuardada(models.Model):
    nombre = models.CharField(max_length=200)
    tabla_html = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
