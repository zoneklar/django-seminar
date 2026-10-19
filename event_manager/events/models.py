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




class Event(models.Model):
    """Der Event, der auf einen bestimmten Zeitpunkt terminiert ist."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="events",  # z.B. sport.events.all()
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Events"

    def __str__(self) -> str:
        return self.name