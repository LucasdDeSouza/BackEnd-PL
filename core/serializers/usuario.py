
from rest_framework.serializers import ModelSerializer

from core.models import usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = usuario
        fields = "__all__"