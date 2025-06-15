# orders/serializers.py
from rest_framework import serializers
from .models import Orders, OrderItems
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItems
        fields = ('product', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Orders
        fields = ('id','status','payment_method','delivery_method','created_at','items','total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()
