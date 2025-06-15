# # orders/admin.py

from django.contrib import admin
from django.urls import path
from django.db.models import Sum, Count
from django.utils.timezone import now, timedelta
from django.shortcuts import render
from .models import OrderStatus, PaymentMethods, DeliveryMethods, Orders, OrderItems, Reviews


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(DeliveryMethods)
class DeliveryMethodsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "payment_method", "delivery_method", "created_at", "total_order_price")
    list_display_links = ("id", "user")
    list_filter = ("status", "payment_method", "delivery_method", "created_at")
    search_fields = ("user__username",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("user",)
    inlines = [OrderItemsInline]

    @admin.display(description="Сумма заказа")
    def total_order_price(self, obj):
        return obj.get_total_price()

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(orders_dashboard), name="orders-dashboard"),
        ]
        return custom_urls + urls


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")
    list_filter = ("order", "product")
    raw_id_fields = ("order", "product")


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "comment_preview", 'created_at')
    list_filter = ("rating",)
    search_fields = ("user__username", "product__name", "comment")
    # filter_horizontal = ("product",)

    @admin.display(description="Комментарий (предпросмотр)")
    def comment_preview(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment


# Кастомная вьюха для дэшборда
def orders_dashboard(request):
    from .models import Orders

    # Общая сумма продаж
    total_sales = sum(order.get_total_price() for order in Orders.objects.all())

    # Общее количество заказов
    total_orders = Orders.objects.count()

    # Количество уникальных пользователей
    unique_users = Orders.objects.values('user').distinct().count()

    # Заказы за последние 7 дней
    today = now().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    daily_sales = []

    for day in last_7_days:
        orders = Orders.objects.filter(created_at__date=day)
        total = sum(order.get_total_price() for order in orders)
        daily_sales.append({'date': day.strftime('%d.%m'), 'total': total})

    context = {
        'total_sales': total_sales,
        'total_orders': total_orders,
        'unique_users': unique_users,
        'daily_sales': daily_sales,
    }

    return render(request, 'admin/orders_dashboard.html', context)

