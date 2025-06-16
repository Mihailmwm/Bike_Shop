# api_urls.py

from rest_framework.routers                   import DefaultRouter
from orders.views                             import OrderViewSet
from products.views import ProductViewSet
from rest_framework_simplejwt.views           import TokenObtainPairView, TokenRefreshView
from users.views                              import RegisterView, UserDetailView, LogoutView
from .api_viewsets                            import CartViewSet, ContactViewSet, ReviewsViewSet
from orders.views import UserReviewsView
from django.urls import path
from orders.views import UserReviewsView


router = DefaultRouter()

router.register(r'orders',        OrderViewSet,         basename='orders')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart',          CartViewSet,          basename='cart')
# router.register(r'reviews',       ReviewsViewSet,       basename='reviews')
router.register(r'contact',       ContactViewSet,       basename='contact-send')

# # JWT и auth
# router.register(r'token',         TokenObtainPairView,  basename='token')
# router.register(r'token/refresh', TokenRefreshView,     basename='token-refresh')
# router.register(r'register',      RegisterView,         basename='register')
# router.register(r'user',          UserDetailView,       basename='current-user')
# router.register(r'logout',        LogoutView,           basename='logout')

urlpatterns = [
    path('reviews/user/', UserReviewsView.as_view(), name='user-reviews'),
]
urlpatterns = router.urls
