# orders/admin.py
# from django.contrib import admin
# from .models import OrderStatus, PaymentMethods, DeliveryMethods, Orders, OrderItems, Reviews

# admin.site.register(OrderStatus)
# admin.site.register(PaymentMethods)
# admin.site.register(DeliveryMethods)
# admin.site.register(Orders)
# admin.site.register(OrderItems)
# admin.site.register(Reviews)

from django.contrib import admin
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
    list_display = ("id", "user", "status", "payment_method", "delivery_method", "created_at")
    list_display_links = ("id", "user")
    list_filter = ("status", "payment_method", "delivery_method", "created_at")
    search_fields = ("user__username",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("user",)
    inlines = [OrderItemsInline]


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")
    list_filter = ("order", "product")
    raw_id_fields = ("order", "product")


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "comment_preview")
    list_filter = ("rating",)
    search_fields = ("user__username", "product__name", "comment")
    # filter_horizontal = ("product",)

    @admin.display(description="Комментарий (предпросмотр)")
    def comment_preview(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
