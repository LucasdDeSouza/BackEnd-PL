from django.db import models
from uploader.models import Image
from .proprietario import Proprietario

class Propriedade(models.Model):
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT, related_name="proprietarios")
    capa = models.ForeignKey(
        Image,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.id} - {self.endereco}"