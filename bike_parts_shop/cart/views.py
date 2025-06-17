# # cart/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .serializers import CartSerializer, CartItemSerializer
# from .models import CartItem
# from products.models import Product

# class CartView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         serializer = CartSerializer(request.user)
#         return Response(serializer.data)

#     def post(self, request):
        
#         product_id = request.data.get('product_id')
#         qty = request.data.get('quantity', 1)
#         try:
#             product = Product.objects.get(pk=product_id)
#         except Product.DoesNotExist:
#             return Response({'detail': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)

#         item, created = CartItem.objects.get_or_create(
#             user=request.user,
#             product=product,
#             defaults={'quantity': qty}
#         )
#         if not created:
#             item.quantity += int(qty)
#             item.save()

#         return Response({'detail': 'Добавлено в корзину'}, status=status.HTTP_201_CREATED)

#     def delete(self, request, product_pk=None):
#         # ожидаем URL /api/cart/{product_pk}/
#         try:
#             item = CartItem.objects.get(user=request.user, product_id=product_pk)
#             item.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except CartItem.DoesNotExist:
#             return Response({'detail': 'Элемент не найден'}, status=status.HTTP_404_NOT_FOUND)


# cart/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import CartSerializer, CartItemSerializer
from .models import CartItem
from products.models import Product

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = CartSerializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        qty = request.data.get('quantity', 1)
        try:
            qty = int(request.data.get('quantity', 1))
            # product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)


        item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': qty}
        )
        if not created:
            item.quantity += int(qty)
            item.save()

        return Response({'detail': 'Добавлено в корзину'}, status=status.HTTP_201_CREATED)

    def delete(self, request, product_pk=None):
        # ожидаем URL /api/cart/{product_pk}/
        try:
            item = CartItem.objects.get(user=request.user, product_id=product_pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Элемент не найден'}, status=status.HTTP_404_NOT_FOUND)
