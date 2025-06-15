from rest_framework.routers                   import DefaultRouter
from orders.views                             import OrderViewSet
from products.views import ProductViewSet
from rest_framework_simplejwt.views           import TokenObtainPairView, TokenRefreshView
from users.views                              import RegisterView, UserDetailView, LogoutView
from .api_viewsets                            import CartViewSet, FavoritesViewSet, ContactViewSet, ReviewsViewSet

router = DefaultRouter()

router.register(r'orders',        OrderViewSet,         basename='orders')
router.register(r'products', ProductViewSet, basename='products')
# router.register(r'cart',          CartViewSet,          basename='cart')
# router.register(r'favorites',     FavoritesViewSet,     basename='favorites')
# router.register(r'reviews',       ReviewsViewSet,       basename='reviews')
# router.register(r'contact',       ContactViewSet,       basename='contact-send')

# # JWT и auth
# router.register(r'token',         TokenObtainPairView,  basename='token')
# router.register(r'token/refresh', TokenRefreshView,     basename='token-refresh')
# router.register(r'register',      RegisterView,         basename='register')
# router.register(r'user',          UserDetailView,       basename='current-user')
# router.register(r'logout',        LogoutView,           basename='logout')

urlpatterns = router.urls
