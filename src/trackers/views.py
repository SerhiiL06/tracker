from datetime import datetime

from rest_framework import viewsets

from . import serializers as sr
from .models import Campaign, Click, Lead, Offer


class CampaignViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Campaign.objects.filter(end_date__gte=datetime.now())
    serializer_class = sr.CampaignListSerializer

    def get_queryset(self):

        if self.request.GET.get("full"):
            return Campaign.objects.all()

        return super().get_queryset()


class OfferViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    lookup_field = "slug"
    queryset = Offer.objects.select_related("campaign")
    serializer_class = sr.OfferListSerializer


class LeadViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Lead.objects.all()
    serializer_class = sr.LeadListSerializer


class ClickViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Click.objects.all()
    serializer_class = sr.ClickListSerializer
