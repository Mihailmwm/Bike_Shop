# cart/serializers.py
from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity']

class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True)

    def to_representation(self, instance):
        # instance — это пользователь request.user
        items = instance.cart_items.all()
        return {'items': CartItemSerializer(items, many=True).data}
