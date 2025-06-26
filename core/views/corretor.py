from rest_framework.viewsets import ModelViewSet

from core.models import Corretor
from core.serializers import CorretorSerializer

class CorretorViewSet(ModelViewSet):
    queryset = Corretor.objects.all()
    serializer_class = CorretorSerializer