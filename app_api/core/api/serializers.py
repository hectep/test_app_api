from rest_framework.serializers import ModelSerializer, ReadOnlyField

from core.utils import generate_api_key
from core.models import App


class AppModelSerializer(ModelSerializer):
    api_key = ReadOnlyField()

    class Meta:
        model = App
        fields = '__all__'

    def create(self, validated_data):
        validated_data['api_key'] = generate_api_key()
        return super(AppModelSerializer, self).create(validated_data)


class ReadOnlyModelSerializer(ModelSerializer):
    """
    Serializer used to return only regenerated api_key
    """

    class Meta:
        model = App
        fields = ('api_key',)
        read_only_fields = ('api_key',)
