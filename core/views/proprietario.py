from rest_framework.viewsets import ModelViewSet

from core.models import Proprietario
from core.serializers import ProprietarioSerializer

class ProprietarioViewSet(ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer