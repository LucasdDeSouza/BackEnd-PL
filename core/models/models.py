from django.db import models

class Modelo3D(models.Model):
    nome = models.CharField(max_length=100)
    arquivo_glb = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Modelo 3D'
        verbose_name_plural = 'Modelos 3D'