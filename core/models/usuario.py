from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14, default='')
    senha = models.CharField(max_length=100)
    datanasc = models.DateField()
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.id} - {self.nome}"