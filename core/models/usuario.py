from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=100),
    cpf = models.CharField(max_length=100),
    senha = models.CharField(max_length=100),
    datanasc = models.CharField(max_length=100),
    nome = models.CharField(max_length=100),
    sobrenome = models.CharField(max_length=100),
    telefone = models.CharField(max_length=100),

    def __str__(self):
        return f"{self.id} - {self.nome} {self.sobrenome}"