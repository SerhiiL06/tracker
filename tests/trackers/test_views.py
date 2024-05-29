from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from src.trackers.common import ClickAction, Interests
from src.trackers.models import Campaign, Lead, Offer


class TestCampaignView(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            username="admin",
            password="qwerty",
        )

        self.headers = {
            "REMOTE_ADDR": "test-address",
            "HTTP_USER_AGENT": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            ),
        }

        campaign_data = {
            "title": "test",
            "description": "test",
            "start_date": "2021-01-01",
            "end_date": "2026-02-01",
        }

        Campaign.objects.create(**campaign_data)

    def test_create_campaign(self):

        camp_data = {
            "title": "test1",
            "description": "test1",
            "start_date": "2020-01-01",
            "end_date": "2020-02-01",
        }

        response = self.client.post(reverse("campaigns-list"), data=camp_data)
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)

        response = self.client.post(reverse("campaigns-list"), data=camp_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Campaign.objects.count(), 2)

    def test_get_campaign_list(self):

        response = self.client.get(reverse("campaigns-list"), **self.headers)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()), 1)


class TestOfferView(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            username="admin",
            password="qwerty",
        )

        self.headers = {
            "REMOTE_ADDR": "test-address",
            "HTTP_USER_AGENT": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            ),
        }

        campaign_data = {
            "title": "test",
            "description": "test",
            "start_date": "2021-01-01",
            "end_date": "2026-02-01",
        }

        self.campaign = Campaign.objects.create(**campaign_data)

        offer_data = {"title": "test", "description": "test", "campaign": self.campaign}

        Offer.objects.create(**offer_data)

    def test_create_offer(self):
        offer_data = {
            "title": "test2",
            "description": "test2",
            "campaign_id": self.campaign.id,
        }

        resposne = self.client.post(reverse("offers-list"), data=offer_data)

        self.assertEqual(resposne.status_code, 403)

        self.client.force_login(self.user)
        resposne = self.client.post(reverse("offers-list"), data=offer_data)

        self.assertEqual(resposne.status_code, 201)

        self.assertEqual(Offer.objects.count(), 2)

    def test_get_offers(self):

        response = self.client.get(reverse("offers-list"), **self.headers)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Lead.objects.count(), 1)

    def test_get_offer(self):
        offer = Offer.objects.first()

        response = self.client.get(offer.offer_link, **self.headers)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Lead.objects.count(), 1)
