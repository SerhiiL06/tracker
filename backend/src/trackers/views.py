from datetime import datetime

from django_filters import rest_framework as filters
from drf_spectacular import types
from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   extend_schema)
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from . import serializers as sr
from .models import Campaign, Click, Lead, Offer


class CampaignViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Campaign.objects.all()
    serializer_class = sr.CampaignListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["title"]
    ordering_fields = ["end_date"]

    def get_queryset(self):

        if self.request.GET.get("full", False):
            return super().get_queryset()

        return Campaign.objects.filter(end_date__gte=datetime.now())

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
            ),
            OpenApiParameter(
                "title",
                description="searching by title text",
                type=types.OpenApiTypes.STR,
                required=False,
            ),
            OpenApiParameter(
                "ordering",
                description="order by end date",
                examples=[OpenApiExample("end_date", "-end_date")],
                type=types.OpenApiTypes.DATE,
                required=False,
            ),
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

    def get_queryset(self):
        queryset = super().get_queryset()
        camp_id = self.request.GET.get("camp_id")
        if self.action == "list" and camp_id:
            return queryset.filter(campaign_id=camp_id)
        return queryset


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
