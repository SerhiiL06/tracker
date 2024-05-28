from django import models


class Interests(models.TextChoices):
    low = "LOW"
    middle = "MIDDLE"
    high = "HIGH"
