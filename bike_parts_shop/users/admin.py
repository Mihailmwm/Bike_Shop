# users/admin.py
from django.contrib import admin
from .models import UserRoles, User

@admin.register(UserRoles)
class UserRolesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    list_display_links = ("username",)
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active")
    readonly_fields = ("last_login", "date_joined")
