# contact/urls.py
from django.urls import path, include
from .views import ContactMessageView

urlpatterns = [
    path('send/', ContactMessageView.as_view(), name='send-message'),

]
