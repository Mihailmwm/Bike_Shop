from django.db.models import Count, Avg, Sum
from django.template.response import TemplateResponse
from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ProductImage
from django.urls import reverse, path
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from django.conf import settings


class ProductImageInline(admin.TabularInline):  # Или admin.StackedInline
    model = ProductImage
    extra = 1  # Количество дополнительных полей для загрузки изображений


class PriceRangeFilter(admin.SimpleListFilter):
    title = "Диапазон цен"
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        return [
            ("low", "До 500"),
            ("medium", "500 - 5000"),
            ("high", "Выше 5000"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "low":
            return queryset.filter(price__lt=500)
        elif self.value() == "medium":
            return queryset.filter(price__gte=500, price__lt=5000)
        elif self.value() == "high":
            return queryset.filter(price__gte=5000)
        return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "price", "category", "available", 'stock',
        "duplicate_link", "download_pdf_link", 'created_at'
    )
    list_display_links = ("name",)
    list_filter = ("category", "available", PriceRangeFilter)
    search_fields = ("name", "description")
    actions = ["duplicate_products", "download_selected_pdfs"]
    inlines = [ProductImageInline]
    change_list_template = "admin/products/product_changelist.html"
    readonly_fields = []

    def changelist_view(self, request, extra_context=None):
        if "duplicate" in request.GET:
            product_id = request.GET.get("duplicate")
            try:
                product = Product.objects.get(id=product_id)
                product.pk = None
                product.name += " (копия)"
                product.save()
                self.message_user(
                    request,
                    f'Товар "{product.name}" успешно скопирован.'
                )
            except Product.DoesNotExist:
                self.message_user(request, "Товар не найден", level='error')

        stats = Product.objects.aggregate(
            avg_price=Avg('price'),
            total_value=Sum('price')
        )

        category_counts = Product.objects.values('category__name').annotate(
            count=Count('id')
        ).order_by('-count')
        category_counts_list = [(item['category__name'], item['count']) for item in category_counts]
        has_cheap_products = Product.objects.filter(price__lt=500).exists()

        extra_context = extra_context or {}
        extra_context.update({
            'avg_price': stats['avg_price'],
            'total_value': stats['total_value'],
            'category_counts': category_counts,
            'category_counts_list': category_counts_list,
            'has_cheap_products': has_cheap_products,
        })

        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'download_pdf/<int:product_id>/',
                self.admin_site.admin_view(self.download_pdf_view),
                name="product_download_pdf"
            ),
        ]
        return custom_urls + urls

    def download_pdf_view(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = (
            f'attachment; filename="{product.name}.pdf"'
        )

        p = canvas.Canvas(response)

        # Определяем путь к шрифту
        font_path = os.path.join(
            settings.BASE_DIR,
            'static', 'fonts', 'roboto.ttf'
        )
        try:
            pdfmetrics.registerFont(TTFont('Roboto', font_path))
            p.setFont('Roboto', 12)
        except Exception as e:
            print(f"Ошибка регистрации шрифта: {e}")
            p.setFont('Helvetica', 12)

        p.drawString(100, 750, f"Продукт: {product.name}")
        p.drawString(
            100, 730,
            f"Доступность: {'Да' if product.available else 'Нет'}"
        )
        p.showPage()
        p.save()

        return response

    @admin.display(description="Скачать PDF")
    def download_pdf_link(self, obj):
        url = reverse(
            "admin:product_download_pdf", args=[obj.id]
        )
        return format_html(
            '<a href="{}" class="button"> Скачать PDF</a>',
            url
        )

    @admin.action(description="Скачать PDF для выбранных товаров")
    def download_selected_pdfs(self, request, queryset):
        from io import BytesIO
        import zipfile

        # Тот же шрифт и регистрация
        font_path = os.path.join(
            settings.BASE_DIR,
            'static', 'fonts', 'roboto.ttf'
        )
        try:
            pdfmetrics.registerFont(TTFont('Roboto', font_path))
        except Exception as e:
            print(f"Ошибка регистрации шрифта: {e}")

        buffer = BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zf:
            for product in queryset:
                pdf_io = BytesIO()
                p = canvas.Canvas(pdf_io)
                try:
                    p.setFont('Roboto', 12)
                except Exception:
                    p.setFont('Helvetica', 12)

                p.drawString(100, 750, f"Продукт: {product.name}")
                p.drawString(
                    100, 730,
                    f"Доступность: {'Да' if product.available else 'Нет'}"
                )
                p.showPage()
                p.save()
                pdf_io.seek(0)
                zf.writestr(f"{product.name}.pdf", pdf_io.read())

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/zip')
        response['Content-Disposition'] = (
            'attachment; filename="products.zip"'
        )
        return response

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return ['created_at']

    @admin.action(description="Копировать выбранные товары")
    def duplicate_products(self, request, queryset):
        for product in queryset:
            product.pk = None
            product.name += ' (копия)'
            product.save()
        self.message_user(
            request,
            'Выбранные товары успешно скопированы.'
        )

    @admin.display(description="Дублирование")
    def duplicate_link(self, obj):
        return format_html(
            '<a href="?duplicate={id}" class="button">Копировать</a>',
            id=obj.id
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
