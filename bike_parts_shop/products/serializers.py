# product/serializers.py
# from rest_framework import serializers
# from .models import Product, Category

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Product
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'image', 'price', 'description')

#     def get_image(self, obj):
#         request = self.context.get('request')
#         if obj.image:
#             return request.build_absolute_uri(obj.image.url)
#         return None

from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
