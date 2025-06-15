from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import RegisterView, UserDetailView, LogoutView

urlpatterns = [
    # получение / обновление токенов
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # регистрация
    path('api/register/', RegisterView.as_view(), name='register'),
    # получить текущего пользователя
    path('api/user/', UserDetailView.as_view(), name='current_user'),
    # логаут (через блэклист)
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
