from django.contrib import admin
from django.urls    import path, include
from django.conf    import settings
from django.conf.urls.static import static

# JWT & auth views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, UserDetailView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Orders ViewSet root
    path('api/', include('bike_parts_shop.api_urls')),


    path('api/cart/', include('cart.urls')),

    path('api/contact/', include('contact.urls')),
    path('api/', include('orders.urls')),  # reviews

    # JWT & auth
    path('api/token/',         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),    name='token_refresh'),
    path('api/register/',      RegisterView.as_view(),        name='register'),
    path('api/user/',          UserDetailView.as_view(),      name='current_user'),
    path('api/logout/',        LogoutView.as_view(),          name='logout'),

    # (ваши HTML-роуты ниже)
    path('', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
