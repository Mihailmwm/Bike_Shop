# orders/urls.py
from django.urls import path
from . import views
from .views import UserReviewsView

urlpatterns = [
    # path('orders/', views.order_list, name='order_list'),
    # path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('reviews/user/', UserReviewsView.as_view(), name='user-reviews'),
]
