# # products/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):  # Или admin.StackedInline
    model = ProductImage
    extra = 1  # Количество дополнительных полей для загрузки изображений

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "available", "duplicate_link")
    list_display_links = ("name",)
    list_filter = ("category", "available")
    search_fields = ("name", "description")
    actions = ["duplicate_products"]
    inlines = [ProductImageInline]

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
