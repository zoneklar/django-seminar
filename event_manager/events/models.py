from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    """Eine Kategorie für einen Event."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)  # mandatory
    # null = True => darf in der DB NULL sein, blank=True => Formularfeld darf leer sein
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    """Der Event, der auf einen bestimmten Zeitpunkt terminiert ist."""

    class Group(models.IntegerChoices):
        SMALL = 2, "kleine Gruppe"
        MEDIUM = 5, "mittelgroße Gruppe"
        BIG = 10, "große Gruppe"
        LARGE = 20, "sehr große Gruppe"
        UNLIMITED = 0, "ohne Begrenzung"

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
    min_group = models.PositiveIntegerField(
        choices=Group.choices,
        default=Group.UNLIMITED,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",  # bob.events.all()
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Events"

    def related_events(self):
        """
        Ähnliche Events aus der gleichen Kategorie und der selben
        min-group.
        """
        related_events = Event.objects.filter(
            min_group=self.min_group,
            category=self.category,
        )
        return related_events.exclude(pk=self.id)

    def __str__(self) -> str:
        return self.name
