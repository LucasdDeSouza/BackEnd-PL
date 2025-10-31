from django.db import models
from requests import delete
from .user import User

class Proprietario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="proprietarios")

    def __str__(self):
        return f"{self.usuario}"
    