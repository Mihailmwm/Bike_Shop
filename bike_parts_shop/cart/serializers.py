# cart/serializers.py

from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # <-- добавили id
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']  # вместо user

class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)

    def to_representation(self, instance):
        # instance — это request.user
        items = instance.cart_items.all()
        return {'items': CartItemSerializer(items, many=True).data}
