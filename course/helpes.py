import uuid
from django.db.models import TextChoices


class PriceType(TextChoices):
    dollar = "USD", "$"
    sum = "UZS", "so'm"
