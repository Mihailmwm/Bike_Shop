# products/views.py
# from django_filters import rest_framework as filters
# from rest_framework import generics, viewsets
# from .models import Product
# from .serializers import ProductSerializer

# from django.shortcuts import render
# from rest_framework.filters import SearchFilter


# class ProductListView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# def product_list_page(request):
#     products = Product.objects.filter(available=True)  # Показываем только доступные товары
#     return render(request, 'products/product_list.html', {'products': products})



# class ProductFilter(filters.FilterSet):
#     speed_count =  filters.BaseInFilter(field_name="speed_count", lookup_expr="in")

#     class Meta:
#         model = Product
#         fields = ['speed_count']

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_class = ProductFilter

from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView


class ProductFilter(filters.FilterSet):
    speed_count = filters.BaseInFilter(field_name="speed_count", lookup_expr="in")

    class Meta:
        model = Product
        fields = ['speed_count']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']


def product_list_page(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer