from datetime import datetime

from rest_framework import serializers

from .models import Campaign, Click, Lead, Offer


class CampaignListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"


class OfferListSerializer(serializers.ModelSerializer):
    campaign = serializers.SerializerMethodField()
    slug = serializers.CharField(read_only=True)
    campaign_id = serializers.IntegerField()

    class Meta:
        model = Offer
        fields = ["title", "slug", "description", "campaign", "campaign_id"]

    def get_campaign(self, obj):
        return obj.campaign.title


class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class ClickListSerializer(serializers.ModelSerializer):
    lead_info = serializers.SerializerMethodField()
    click_on = serializers.SerializerMethodField()

    class Meta:
        model = Click
        fields = [
            "id",
            "campaign",
            "offer",
            "lead",
            "lead_info",
            "click_on",
            "interest_level",
            "action",
        ]

    def get_lead_info(self, obj):
        return obj.lead.ip_address

    def get_click_on(self, obj):
        return obj.click_on.ctime()
