def normalize_name(name: str) -> str:
    """Löscht überschüssige Leerzeichen aus einem String.
    Ein Beispiel für das Normalisieren eines Name-Strings.
    """
    return " ".join(name.split())
