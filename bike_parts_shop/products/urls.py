# products/urls.py
# from django.urls import path, include
# from .views import product_list_page, ProductViewSet
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'products', ProductViewSet)

# urlpatterns = [
#     #API
#     path('api/', include(router.urls)),
#     # path('api/products/', ProductListView.as_view(), name='product_list'),
#     # path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

#     # HTML-страница
#     path('', product_list_page, name='product_list_page'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list_page, ProductListView

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Должен автоматически создать '/api/products/'

urlpatterns = [
    # API маршруты
    path('api/', include(router.urls)),  # Оставляем только router.urls

    # HTML-страница
    path('products/', ProductListView.as_view(), name='product-list'),
    path('', product_list_page, name='product_list_page'),
]

