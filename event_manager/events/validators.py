from django.core.exceptions import ValidationError


def check_illegal(value: str) -> None:
    """Löst ValidationError aus, wenn ein * in value ist."""
    if "*" in value:
        raise ValidationError("Der String darf kein * enthalten.")
