from django.db import models

class Propriedade(models.Model):
    endereco = models.CharField(max_length=100)
    completmento = models.CharField(max_length=100),
    estado = models.CharField(max_length=100),
    cep = models.CharField(max_length=100),
    cidade = models.CharField(max_length=100),

    def __str__(self):
        return self.id