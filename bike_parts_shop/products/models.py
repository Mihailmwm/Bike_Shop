# product/models.py

from django.db import models

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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
