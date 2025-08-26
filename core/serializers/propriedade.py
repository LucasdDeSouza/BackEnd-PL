
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField


from core.models import Propriedade

from uploader.models import Image
from uploader.serializers import ImageSerializer

class PropriedadeSerializer(ModelSerializer):
    class Meta:
        model = Propriedade
        fields = "__all__"

class PropriedadeRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Propriedade
        fields = '__all__'
        depth = 1
...
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Propriedade
        fields = '__all__'