# product/serializers.py

# from rest_framework import serializers
# from .models import Product, Category

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_image(self, obj):
#         request = self.context.get('request')
#         if obj.image:
#             return request.build_absolute_uri(obj.image.url)
#         return None

# -----------------------------------------------------

from rest_framework import serializers
from .models import Product, Category, ProductImage  # Добавил ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений товара"""
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True, read_only=True)  # Изменил image → images

    class Meta:
        model = Product
        fields = '__all__'
