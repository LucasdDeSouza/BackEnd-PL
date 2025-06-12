
from rest_framework.serializers import ModelSerializer

from core.models import proprietario

class ProprietarioSerializer(ModelSerializer):
    class Meta:
        model = proprietario
        fields = "__all__"