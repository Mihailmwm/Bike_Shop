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

urlpatterns = [
    path('admin/', admin.site.urls),

    # Все DRF-маршруты здесь
    path('api/', include('bike_parts_shop.api_urls')),

    # Ваши HTML-вьюхи
    path('', include('products.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
