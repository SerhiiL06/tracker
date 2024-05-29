from django.db import models
from django.urls import reverse
from slugify import slugify

from .common import Interests


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


class Offer(models.Model):

    title = models.CharField(max_length=100)
    slug = models.CharField()
    description = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def offer_link(self):
        return reverse("trackers:offer", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title


class Lead(models.Model):

    ip_address = models.CharField(unique=True)
    agent = models.CharField()

    is_hot = models.BooleanField(default=False)


class Click(models.Model):

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True)

    click_on = models.DateTimeField(auto_now_add=True)

    interest_level = models.CharField(choices=Interests.choices, default=Interests.low)

    def __str__(self) -> str:
        return f"{self.lead} click {self.offer}"
