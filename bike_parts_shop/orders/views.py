# orders/views.py
from django.shortcuts import render
from .models import Orders

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Orders.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
