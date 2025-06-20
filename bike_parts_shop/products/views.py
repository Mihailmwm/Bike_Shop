# # products/views.py

#     # ----------------------------------------------

# from django_filters import rest_framework as filters
# from rest_framework import viewsets
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.shortcuts import render, get_object_or_404, redirect

# from rest_framework.response import Response
# from rest_framework import status

# from .forms import ProductForm

# from django.views.generic import DetailView
# from .models import Product, ProductImage
# from .serializers import ProductSerializer

# class ProductFilter(filters.FilterSet):
#     speed_count = filters.BaseInFilter(field_name="speed_count", lookup_expr="in")
#     # available = filters.BooleanFilter(field_name="available")  # Добавляем фильтр
    
#     class Meta:
#         model = Product
#         fields = ['speed_count']

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_class = ProductFilter
#     search_fields = ['name', 'description']
#     parser_classes = (MultiPartParser, FormParser)  # Для загрузки файлов

#     def create(self, request, *args, **kwargs):
#         """Создание товара с несколькими изображениями"""
#         product_serializer = ProductSerializer(data=request.data)
#         if product_serializer.is_valid():
#             product = product_serializer.save()
            
#             # Сохранение изображений
#             images = request.FILES.getlist('images')
#             for image in images:
#                 ProductImage.objects.create(product=product, image=image)

#             return Response(product_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def product_list_page(request):
#     # products = Product.objects.filter(available=True)
#     # return render(request, 'products/product_list.html', {'products': products})
#     products = Product.objects.filter(available=True).exclude(category__name="Архив").order_by('-price')
#     return render(request, 'products/product_list.html', {'products': products})

# class ProductListView(ListAPIView):
#     # queryset = Product.objects.all()
#     # serializer_class = ProductSerializer
#     queryset = Product.objects.filter(available=True).exclude(category__name="Архив").order_by('-created_at')
#     serializer_class = ProductSerializer


# # class ProductDetailView(DetailView):
# #     model = Product
# #     # template_name = "products/product_detail.html"
# #     context_object_name = "product"  

# class ProductDetailView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# # ---------------------------------------------------------------------

# def product_list(request):
#     products = Product.objects.select_related('category').all()
#     return render(request, 'products/product_list.html', {'products': products})

# def product_create(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('product_list')
#     return render(request, 'products/product_form.html', {'form': form})

# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = ProductForm(request.POST or None, instance=product)
#     if form.is_valid():
#         form.save()
#         return redirect('product_list')
#     return render(request, 'products/product_form.html', {'form': form})

# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'products/product_confirm_delete.html', {'product': product})

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .forms import ProductForm
from .models import Product, ProductImage
from .serializers import ProductSerializer

from orders.models import OrderItems
from django.db.models import Sum


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
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        """Создание товара с несколькими изображениями"""
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product = product_serializer.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def product_list_page(request):
    products = Product.objects.filter(available=True).exclude(category__name="Архив").order_by('-price')
    return render(request, 'products/product_list.html', {'products': products})


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(available=True).exclude(category__name="Архив").order_by('-created_at')
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'products/product_list.html', {'products': products})


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})




@api_view(['GET'])
def products_by_speed(request):
    grouped = {
        6: [],
        9: [],
        12: [],
    }

    products = Product.objects.filter(speed_count__in=[6, 9, 12], available=True)
    serializer = ProductSerializer(products, many=True)

    for product in serializer.data:
        speed = product.get("speed_count")
        if speed in grouped:
            grouped[speed].append(product)

    return Response(grouped)
