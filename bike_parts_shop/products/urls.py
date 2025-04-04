# products/urls.py


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list_page, ProductListView, ProductDetailView  

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Должен автоматически создать '/api/products/'
# router.register(r'categories', CategoryViewSet, basename='category')  # Добавляем роут

urlpatterns = [
    # API маршруты
    path('api/', include(router.urls)),  

    # HTML-страница
    path('products/', ProductListView.as_view(), name='product-list'),
    path('', product_list_page, name='product_list_page'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

