# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserRoles(models.Model):
    name = models.CharField(max_length=50, verbose_name="Роль пользователя")

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

    def __str__(self):
        return self.name


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        verbose_name="Группы"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
        verbose_name="Права доступа"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


