# orders/serializers.py
from rest_framework import serializers
from .models import Orders, OrderItems
from products.serializers import ProductSerializer
from .models import Reviews

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
    
class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_image = serializers.ImageField(source='product.image', read_only=True)  # если у продукта есть поле image

    class Meta:
        model = Reviews
        fields = ['id', 'product', 'product_name', 'product_image', 'rating', 'comment', 'created_at']