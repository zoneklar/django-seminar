from django.db import models


class Category(models.Model):
    """Eine Kategorie für einen Event."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)  # mandatory
    # null = True => darf in der DB NULL sein, blank=True => Formularfeld darf leer sein
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
