# # products/admin.py

from django.db.models import Count, Avg, Sum
from django.template.response import TemplateResponse

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ProductImage
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.urls import path


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
    list_display = ("name", "price", "category", "available",'stock', "duplicate_link", "download_pdf_link", 'created_at')
    list_display_links = ("name",)
    list_filter = ("category", "available", PriceRangeFilter)
    search_fields = ("name", "description")
    actions = ["duplicate_products", "download_selected_pdfs"]
    inlines = [ProductImageInline]
    change_list_template = "admin/products/product_changelist.html"
    
    # Разрешаем редактирование поля created_at в админке
    readonly_fields = []

    def changelist_view(self, request, extra_context=None):
        # Обработка дублирования
        if "duplicate" in request.GET:
            product_id = request.GET.get("duplicate")
            try:
                product = Product.objects.get(id=product_id)
                product.pk = None
                product.name += " (копия)"
                product.save()
                self.message_user(request, f'Товар "{product.name}" успешно скопирован.')
            except Product.DoesNotExist:
                self.message_user(request, "Товар не найден", level='error')

        # Добавляем статистику
        stats = Product.objects.aggregate(
            avg_price=Avg('price'),
            total_value=Sum('price') 
        )

        category_counts = Product.objects.values('category__name').annotate(
            count=Count('id')
        ).order_by('-count')

        extra_context = extra_context or {}
        extra_context.update({
            'avg_price': stats['avg_price'],
            'total_value': stats['total_value'],
            'category_counts': category_counts,
        })

        return super().changelist_view(request, extra_context=extra_context)




    # def changelist_view(self, request, extra_context=None):
    # # Обработка дублирования
    #     if "duplicate" in request.GET:
    #         product_id = request.GET.get("duplicate")
    #         try:
    #             product = Product.objects.get(id=product_id)
    #             product.pk = None
    #             product.name += " (копия)"
    #             product.save()
    #             self.message_user(request, f'Товар "{product.name}" успешно скопирован.')
    #         except Product.DoesNotExist:
    #             self.message_user(request, "Товар не найден", level='error')

    #     # Добавляем статистику
    #     stats = Product.objects.aggregate(
    #         avg_price=Avg('price'),
    #         total_value=Sum('price' * Sum('stock'))
    # )

    #     category_counts = Product.objects.values('category__name').annotate(
    #         count=Count('id')
    #     ).order_by('-count')

    #     extra_context = extra_context or {}
    #     extra_context.update({
    #         'avg_price': stats['avg_price'],
    #         'total_value': stats['total_value'],
    #         'category_counts': category_counts,
    #     })

    #     return super().changelist_view(request, extra_context=extra_context)


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download_pdf/<int:product_id>/', self.admin_site.admin_view(self.download_pdf_view), name="product_download_pdf"),
        ]
        return custom_urls + urls

    def download_pdf_view(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
        
        # p = canvas.Canvas(response)
        # p.drawString(100, 750, f"Product: {product.name}")
        # p.drawString(100, 730, f"Available: {'Yes' if product.available else 'No'}")
        # p.showPage()
        # p.save()

        # return response

        p = canvas.Canvas(response)
    
        # Путь к шрифту (замените на ваш реальный путь)
        font_path = r"D:\4 семестр\bike_shop\static\fonts\DejaVuSansBoldOblique.ttf"
        
        # Регистрация шрифта
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        try:
            pdfmetrics.registerFont(TTFont('DejaVuSansBoldOblique', font_path))
            p.setFont("DejaVuSansBoldOblique", 12)
        except Exception as e:
            print(f"Ошибка загрузки шрифта: {e}")
            # Fallback на стандартный шрифт, если не удалось загрузить
            p.setFont("Helvetica", 12)
        
        p.drawString(100, 750, f"Продукт: {product.name}")
        p.drawString(100, 730, f"Доступность: {'Да' if product.available else 'Нет'}")
        p.showPage()
        p.save()

        return response

    @admin.display(description="Скачать PDF")
    def download_pdf_link(self, obj):
        """Добавляет кнопку для скачивания PDF в список товаров"""
        url = reverse("admin:product_download_pdf", args=[obj.id])
        return format_html('<a href="{}" class="button">📄 Скачать PDF</a>', url)

    @admin.action(description="Скачать PDF для выбранных товаров")
    def download_selected_pdfs(self, request, queryset):
        """Создает и скачивает ZIP с PDF-файлами для выбранных товаров"""
        from io import BytesIO
        import zipfile
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        # Путь к шрифту
        font_path = r"D:\4 семестр\bike_shop\static\fonts\DejaVuSansBoldOblique..ttf"
    
        # Регистрация шрифта
        try:

            pdfmetrics.registerFont(TTFont('DejaVuSansBoldOblique.', font_path))
        except Exception as e:
            print(f"Ошибка загрузки шрифта: {e}")


        buffer = BytesIO()
        with zipfile.ZipFile(buffer, "w") as zf:
            for product in queryset:
                pdf_io = BytesIO()
                p = canvas.Canvas(pdf_io)
                
                try:
                    p.setFont("DejaVuSansBoldOblique.", 12)
                except:
                    p.setFont("Helvetica", 12)
                
                p.drawString(100, 750, f"Продукт: {product.name}")
                p.drawString(100, 730, f"Доступность: {'Да' if product.available else 'Нет'}")
                p.showPage()
                p.save()
                pdf_io.seek(0)
                zf.writestr(f"{product.name}.pdf", pdf_io.read())

        buffer.seek(0)
        response = HttpResponse(buffer, content_type="application/zip")
        response["Content-Disposition"] = 'attachment; filename="products.zip"'
        return response

        # buffer = BytesIO()
        # with zipfile.ZipFile(buffer, "w") as zf:
        #     for product in queryset:
        #         pdf_io = BytesIO()
        #         p = canvas.Canvas(pdf_io)
        #         p.drawString(100, 750, f"Product: {product.name}")
        #         p.drawString(100, 730, f"Available: {'Yes' if product.available else 'No'}")
        #         p.showPage()
        #         p.save()
        #         pdf_io.seek(0)
        #         zf.writestr(f"{product.name}.pdf", pdf_io.read())

        # buffer.seek(0)
        # response = HttpResponse(buffer, content_type="application/zip")
        # response["Content-Disposition"] = 'attachment; filename="products.zip"'
        # return response

    def get_readonly_fields(self, request, obj=None):
        """Разрешает редактирование created_at при изменении объекта"""
        if obj:  # Если редактируем существующий объект
            return self.readonly_fields
        return ["created_at"]  # При создании объекта поле остаётся неизменяемым


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
    

    # def changelist_view(self, request, extra_context=None):
    #     if "duplicate" in request.GET:
    #         product_id = request.GET.get("duplicate")
    #         product = Product.objects.get(id=product_id)
    #         product.pk = None
    #         product.name += " (копия)"
    #         product.save()
    #         self.message_user(request, f'Товар "{product.name}" успешно скопирован.')
    #     return super().changelist_view(request, extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')