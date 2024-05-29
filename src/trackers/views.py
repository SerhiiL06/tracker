from datetime import datetime

from rest_framework import viewsets

from .models import Campaign, Click, Lead, Offer
from .serializers import (CampaignListSerializer, LeadListSerializer,
                          OfferListSerializer)


class CampaignViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Campaign.objects.all()
    serializer_class = CampaignListSerializer

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(end_date__gte=datetime.now())


class OfferViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Offer.objects.select_related("campaign")
    serializer_class = OfferListSerializer


class LeadViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Lead.objects.all()
    serializer_class = LeadListSerializer
