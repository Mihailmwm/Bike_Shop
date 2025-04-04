# orders/models.py

from django.db import models
from users.models import User
from products.models import Product
from django.utils import timezone 

# Убираем импорт PaymentMethods в начале файла, чтобы избежать циклического импорта
# Вместо этого будем использовать строковый импорт в определении ManyToManyField

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус заказа")

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"

    def __str__(self):
        return self.name


class PaymentMethods(models.Model):
    name = models.CharField(max_length=50, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"

    def __str__(self):
        return self.name


class DeliveryMethods(models.Model):
    name = models.CharField(max_length=50, verbose_name="Метод доставки")

    class Meta:
        verbose_name = "Метод доставки"
        verbose_name_plural = "Методы доставки"

    def __str__(self):
        return self.name


# class ProductPaymentMethods(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
#     payment_method = models.ManyToManyField('PaymentMethods', verbose_name="Способы оплаты")  # Используем строковый импорт для модели PaymentMethods

#     class Meta:
#         verbose_name = "Способы оплаты для товара"
#         verbose_name_plural = "Способы оплаты для товаров"

#     def __str__(self):
#         return f"{self.product.name} - {', '.join([pm.name for pm in self.payment_method.all()])}"  # Показываем все способы оплаты


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="orders")
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, verbose_name="Статус заказа")
    payment_method = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT, null=True, verbose_name="Способ оплаты")
    delivery_method = models.ForeignKey(DeliveryMethods, on_delete=models.PROTECT, null=True, verbose_name="Метод доставки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ {self.id} - {self.user.username}"


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, related_name="items", on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу")

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказов"

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="reviews")
    rating = models.PositiveIntegerField(verbose_name="Рейтинг", choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-id"]

    def __str__(self):
        return f"Отзыв {self.user.username} - {self.product.name}"
