# product/models.py

from django.db import models
from django.utils import timezone 
from django.urls import reverse
from django.db.models import Count, Avg, Sum


# Кастомный менеджер
class ProductManager(models.Manager):
    def available_products(self):
        """Возвращает только доступные товары."""
        return self.filter(available=True)

    def out_of_stock(self):
        """Возвращает товары, которых нет в наличии."""
        return self.filter(stock=0)

    def expensive_products(self, price_limit):
        """Возвращает товары дороже указанной суммы."""
        return self.filter(price__gt=price_limit)

    def update_price(self, new_price):
        """Обновить цену для всех товаров"""
        self.update(price=new_price)

    def average_price(self):
        """Возвращает среднюю цену всех товаров"""
        return self.aggregate(Avg('price'))['price__avg']

    def total_stock_value(self):
        """Возвращает общую стоимость всех товаров (цена * количество)"""
        return self.aggregate(total_value=Sum(models.F('price') * models.F('stock')))['total_value']

    def category_counts(self):
        """Возвращает количество товаров в каждой категории"""
        return self.values('category__name').annotate(count=Count('id')).order_by('-count')
    
    def category_counts_list(self):
        """Возвращает количество товаров в каждой категории в виде списка кортежей (category_name, count)."""
        return self.values_list('category__name').annotate(count=Count('id')).order_by('-count')

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="products")
    stock = models.PositiveIntegerField(verbose_name="Остаток на складе")
    image = models.ImageField(upload_to='product_images/', verbose_name="Изображение")
    available = models.BooleanField(default=True, verbose_name="В наличии")
    speed_count = models.IntegerField(choices=[(6, "6 скоростей"), (9, "9 скоростей"), (12, "12 скоростей")], null=True, blank=True, verbose_name="Число передач")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    # Подключаем кастомный менеджер
    objects = ProductManager()

    def get_absolute_url(self):
        """Возвращает URL для просмотра товара."""
        return reverse('product_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at','price']



    def __str__(self):
        return self.name
    
# ---------------------------------------------------------------------
class ProductImage(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/', verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.product.name}"

