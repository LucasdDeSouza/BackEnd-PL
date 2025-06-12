from rest_framework.viewsets import ModelViewSet

from core.models import Propriedade
from core.serializers import PropriedadeSerializer

class PropriedadeViewSet(ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer