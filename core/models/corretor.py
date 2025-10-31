from django.db import models

from .user import User

class Corretor(models.Model):
    cnpj = models.CharField(max_length=100)
    creci = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    nome = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Usuarios")


    def __str__(self):
        return f"{self.id} - {self.cnpj} - {self.creci} - {self.nome}"