# bike_parts_shop/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, products_by_speed

router = DefaultRouter()
# Регистрируем CRUD-эндпоинты для модели Product
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    # все роуты из ProductViewSet (GET/POST/PUT/PATCH/DELETE /api/products/)
    path('', include(router.urls)),
    # наш кастомный эндпоинт для группировки по передаточным числам
    path('products/by-speed/', products_by_speed, name='products-by-speed'),
]
