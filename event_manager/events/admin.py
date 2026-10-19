from django.contrib import admin
from .models import Category, Event 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Baut auf Basis eines Models Formulare."""
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass