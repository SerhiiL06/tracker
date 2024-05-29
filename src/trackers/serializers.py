from rest_framework import serializers

from .models import Campaign, Lead, Offer


class CampaignListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ["title", "description", "start_date", "end_date"]


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
