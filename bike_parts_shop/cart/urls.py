from django.urls import path
from .views import CartView
# , CartItemDetailView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    # path('item/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
]
