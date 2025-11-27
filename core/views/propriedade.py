from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from core.models import Propriedade
from core.serializers import PropriedadeSerializer

class PropriedadeViewSet(ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
