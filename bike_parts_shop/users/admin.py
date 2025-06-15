# # users/admin.py
# from django.contrib import admin
# from .models import UserRoles, User
# from django.db.models import Count
# from orders.models import Orders 

# @admin.register(UserRoles)
# class UserRolesAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("username", "email", "is_staff", "is_active", "order_count")
#     list_display_links = ("username",)
#     search_fields = ("username", "email")
#     list_filter = ("is_staff", "is_active")
#     readonly_fields = ("last_login", "date_joined")

# # Аннотируем пользователей количеством заказов
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         # Агрегируем количество заказов для каждого пользователя
#         queryset = queryset.annotate(order_count=Count("orders"))
#         return queryset

#     # Отображаем количество заказов в админке
#     @admin.display(description="Количество заказов")
#     def order_count(self, obj):
#         return obj.order_count

