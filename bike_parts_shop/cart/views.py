# cart/views.py  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart = request.user.cart  # ваш метод получения корзины
        serializer = CartSerializer(cart)
        return Response(serializer.data)
