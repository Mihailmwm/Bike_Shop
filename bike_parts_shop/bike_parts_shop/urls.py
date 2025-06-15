# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from products.views import product_list_page

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('products/', include('products.urls')),  
#     path('api/', include('bike_parts_shop.api_urls')),
#     path("product_list_page", product_list_page, name="home"), 
#     path('contact/', include('contact.urls')),

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# bike_parts_shop/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Импорт представлений Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Ваши вьюхи регистрации/пользователя/логаута
from users.views import RegisterView, UserDetailView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Все DRF-маршруты здесь
    path('api/', include('bike_parts_shop.api_urls')),

   

    # Ваши HTML-вьюхи
    path('', include('products.urls')),
    path('contact/', include('contact.urls')),

      # JWT: получение и обновление токенов
    path('api/token/',         TokenObtainPairView.as_view(),  name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),

    # Регистрация, профиль, логаут
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/',     UserDetailView.as_view(), name='current_user'),
    path('api/logout/',   LogoutView.as_view(),     name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
