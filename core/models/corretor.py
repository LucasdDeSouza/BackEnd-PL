from django.db import models

from .usuario import Usuario

class Corretor(models.Model):
    cnpj = models.CharField(max_length=100)
    creci = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    nome = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="Usuarios")


    def __str__(self):
        return f"{self.id} - {self.cnpj} - {self.creci} - {self.nome}"