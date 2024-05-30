from datetime import datetime

from rest_framework import viewsets

from . import serializers as sr
from .models import Campaign, Click, Lead, Offer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular import types
from rest_framework.exceptions import MethodNotAllowed


class CampaignViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Campaign.objects.filter(end_date__gte=datetime.now())
    serializer_class = sr.CampaignListSerializer

    def get_queryset(self):

        if self.request.GET.get("full", False):
            return Campaign.objects.all()

        return super().get_queryset()

    @extend_schema(
        description="This endpoint retrieves a list of campaigns.",
        parameters=[
            OpenApiParameter(
                "full",
                description=(
                    "If the full parameter is not specified or False, the endpoint will return a list of campaigns where the end date is not earlier than today's date."
                ),
                required=False,
                type=types.OpenApiTypes.BOOL,
            )
        ],
        tags=["campaigns"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Endpoint creates a new campaignoint",
        tags=["campaigns"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")


class OfferViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    lookup_field = "slug"
    queryset = Offer.objects.select_related("campaign")
    serializer_class = sr.OfferListSerializer

    @extend_schema(
        description="This endpoint retrieves a list of offers.",
        tags=["campaigns"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class LeadViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Lead.objects.all()
    serializer_class = sr.LeadListSerializer

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")


class ClickViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Click.objects.all()
    serializer_class = sr.ClickListSerializer

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")
