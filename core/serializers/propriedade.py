
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField


from core.models import Propriedade

from uploader.models import Image, Document
from uploader.serializers import ImageSerializer, DocumentSerializer

class PropriedadeSerializer(ModelSerializer):
    class Meta:
        model = Propriedade
        fields = "__all__"

class PropriedadeRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    modelo_3d = DocumentSerializer(required=False)

    class Meta:
        model = Propriedade
        fields = '__all__'
        depth = 1
...
class PropriedadeSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    modelo_3d_attachment_key = SlugRelatedField(
        source='modelo_3d',
        queryset=Document.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    modelo_3d = DocumentSerializer(required=False, read_only=True)

    class Meta:
        model = Propriedade
        fields = '__all__'
