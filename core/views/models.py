from rest_framework.viewsets import ModelViewSet

from core.models import Modelo3D
from core.serializers import ModeloSerializer

class CorretorViewSet(ModelViewSet):
    queryset = Modelo3D.objects.all()
    serializer_class = ModeloSerializer  