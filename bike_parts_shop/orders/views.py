# orders/views.py
from django.shortcuts import render
from .models import Orders
from .serializers import OrderSerializer
from rest_framework import viewsets, permissions

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Reviews
from .serializers import ReviewSerializer

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Orders.objects.get(id=order_id)

    for product in order.products.all():
        print(product.name)
        
    return render(request, 'orders/order_detail.html', {'order': order})

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)
    

class UserReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Reviews.objects.filter(user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)