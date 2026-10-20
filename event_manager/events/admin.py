from django.contrib import admin

from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Baut auf Basis eines Models Formulare."""

    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("category",)
    list_display = ("id", "name", "category", "is_active")
