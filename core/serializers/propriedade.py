
from rest_framework.serializers import ModelSerializer

from core.models import Propriedade

class PropriedadeSerializer(ModelSerializer):
    class Meta:
        model = Propriedade
        fields = "__all__"
