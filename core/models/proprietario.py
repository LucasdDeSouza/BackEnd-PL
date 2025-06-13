from django.db import models
from requests import delete
from .usuario import Usuario

class Proprietario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="proprietarios")

    def __str__(self):
        return f"{self.usuario}"
    