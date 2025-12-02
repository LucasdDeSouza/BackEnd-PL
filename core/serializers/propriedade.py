from rest_framework import serializers
from uploader.models import Image
from core.models import Propriedade

class PropriedadeSerializer(serializers.ModelSerializer):
    capa_arquivo = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Propriedade
        fields = [
            "id",
            "endereco",
            "complemento",
            "estado",
            "cep",
            "cidade",
            "usuario",
            "capa",
            "capa_arquivo",
        ]
        read_only_fields = ["capa"]

    def create(self, validated_data):
        imagem = validated_data.pop("capa_arquivo", None)

        propriedade = Propriedade.objects.create(**validated_data)

        if imagem:
            img = Image.objects.create(file=imagem)
            propriedade.capa = img
            propriedade.save()

        return propriedade
