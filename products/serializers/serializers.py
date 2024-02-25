from rest_framework import serializers
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    owner_first_name = serializers.CharField(source="owner.first_name", read_only=True)
    owner_last_name = serializers.CharField(source="owner.last_name", read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
