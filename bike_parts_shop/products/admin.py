# # products/admin.py

# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Product, Category

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'category', 'available', 'duplicate_link')  # Добавляем ссылку на копирование
#     list_filter = ('category', 'available')
#     search_fields = ('name', 'description')
#     actions = ['duplicate_products']  # Добавляем действие в админку

#     def duplicate_products(self, request, queryset):
#         """
#         Действие для копирования выбранных товаров.
#         """
#         for product in queryset:
#             product.pk = None  # Создаём новый объект без ID
#             product.name += " (копия)"
#             product.save()
#         self.message_user(request, "Выбранные товары успешно скопированы.")
    
#     duplicate_products.short_description = "Копировать выбранные товары"

#     def duplicate_link(self, obj):
#         """
#         Добавляем ссылку "Копировать" в списке товаров.
#         """
#         return format_html('<a href="?duplicate={id}">Копировать</a>', id=obj.id)
    
#     duplicate_link.short_description = "Дублирование"

#     def changelist_view(self, request, extra_context=None):
#         """
#         Обрабатываем параметр `duplicate` в URL, чтобы позволить копирование через ссылку.
#         """
#         if 'duplicate' in request.GET:
#             product_id = request.GET.get('duplicate')
#             product = Product.objects.get(id=product_id)
#             product.pk = None
#             product.name += " (копия)"
#             product.save()
#             self.message_user(request, f'Товар "{product.name}" успешно скопирован.')
#         return super().changelist_view(request, extra_context)
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "available", "duplicate_link")
    list_display_links = ("name",)
    list_filter = ("category", "available")
    search_fields = ("name", "description")
    actions = ["duplicate_products"]

    @admin.action(description="Копировать выбранные товары")
    def duplicate_products(self, request, queryset):
        for product in queryset:
            product.pk = None
            product.name += " (копия)"
            product.save()
        self.message_user(request, "Выбранные товары успешно скопированы.")

    @admin.display(description="Дублирование")
    def duplicate_link(self, obj):
        return format_html(
            '<a href="?duplicate={id}" class="button">Копировать</a>', id=obj.id
        )

    def changelist_view(self, request, extra_context=None):
        if "duplicate" in request.GET:
            product_id = request.GET.get("duplicate")
            product = Product.objects.get(id=product_id)
            product.pk = None
            product.name += " (копия)"
            product.save()
            self.message_user(request, f'Товар "{product.name}" успешно скопирован.')
        return super().changelist_view(request, extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
