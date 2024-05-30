from django.db import models


class Interests(models.TextChoices):
    LOW = "LOW"
    MIDDLE = "MIDDLE"
    HIGH = "HIGH"


class ClickAction(models.TextChoices):
    CAMPAIGN_LIST = "CAMPAIGN_LIST"
    CAMPAIGN_DETAIL = "CAMPAIGN_DETAIL"

    OFFER_LIST = "OFFER_LIST"
    OFFER_DETAIL = "OFFER_DETAIL"
