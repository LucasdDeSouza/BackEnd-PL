
from rest_framework.serializers import ModelSerializer

from core.models import Proprietario

class ProprietarioSerializer(ModelSerializer):
    class Meta:
        model = Proprietario
        fields = "__all__"