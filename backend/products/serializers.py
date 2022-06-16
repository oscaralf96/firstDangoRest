from rest_framework import serializers

from .models import Product

# Create your models here.
class ProductSerializer(serializers.ModelSerializer):
    """You can have multiple serializers for the same model"""
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_discount(self, obj):
        #if not hasattr(obj, 'id'):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
