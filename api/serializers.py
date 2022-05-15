from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    options = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "image",
            "options",
            "category",
            "price",
            "slug",
            "recommend",
            "sales_count",
            "discount_peresen",
            "create",
            "update",
        )


class CartAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quanity = serializers.IntegerField()

