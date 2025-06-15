# favorites/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from products.models import Product
from products.serializers import ProductSerializer

class FavoritesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favs = request.user.favorites.all()  # m2m relationship
        serializer = ProductSerializer(favs, many=True)
        return Response(serializer.data)
