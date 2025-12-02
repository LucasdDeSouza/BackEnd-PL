from rest_framework.serializers import ModelSerializer

from core.models import Modelo3D

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo3D
        fields = "__all__"
