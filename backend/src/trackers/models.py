from django.db import models
from django.urls import reverse
from slugify import slugify

from .common import ClickAction, Interests


class Campaign(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField()
    end_date = models.DateField()

    task = models.CharField(max_length=250, null=True)

    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Offer(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField()
    description = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def offer_link(self):
        return reverse("offers-detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Lead(models.Model):

    ip_address = models.CharField(unique=True)
    agent = models.CharField()
    os = models.CharField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    is_hot = models.BooleanField(default=False)


class Click(models.Model):
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, null=True, related_name="camp_click"
    )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True, related_name="offer_click"
    )

    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True)

    click_on = models.DateTimeField(auto_now_add=True)

    interest_level = models.CharField(choices=Interests.choices, default=Interests.LOW)

    action = models.CharField(
        choices=ClickAction.choices, default=ClickAction.CAMPAIGN_LIST
    )

    def __str__(self) -> str:
        return f"{self.lead} click {self.offer}"

    class Meta:
        ordering = ["-click_on"]
