from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=100)
    cpf = models.IntegerField(default=0)
    senha = models.CharField(max_length=100)
    datanasc = models.DateField(max_length=100)
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.nome}"