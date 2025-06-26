
from rest_framework.serializers import ModelSerializer

from core.models import Corretor

class CorretorSerializer(ModelSerializer):
    class Meta:
        model = Corretor
        fields = "__all__"
