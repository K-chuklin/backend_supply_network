from rest_framework import serializers
from providers.models import Unit
from products.serializers.serializers import ProductSerializer


class ProviderSerializer(serializers.ModelSerializer):
    owner_first_name = serializers.CharField(source="owner.first_name", read_only=True)
    owner_last_name = serializers.CharField(source="owner.last_name", read_only=True)
    product = ProductSerializer(many=True, required=False)
    Unit = serializers.SlugRelatedField(slug_field='Name', queryset=Unit.objects.all())

    class Meta:
        model = Unit
        fields = '__all__'
