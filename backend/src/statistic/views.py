from django.db.models import Count
from django.db.models.functions import TruncDay
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from src.trackers.models import Click, Lead, Offer

from . import serializers as sr


@extend_schema_view(list=extend_schema(tags=["statistic"]))
class StatisticViewSet(viewsets.GenericViewSet):
    queryset = Click.objects.all()

    @action(methods=["get"], detail=False, url_path="clicks-per")
    def sum_clicks_per_day(self, request, *args, **kwargs):

        q = (
            Click.objects.annotate(date=TruncDay("click_on"))
            .values("date")
            .annotate(count=Count("id"))
        )

        serializer = sr.ClickPerDaySerializer(q, many=True)

        return Response(serializer.data, 200)

    @action(methods=["get"], detail=False, url_path="leads-per")
    def sum_leads_per_day(self, request, *args, **kwargs):

        q = (
            Lead.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(count=Count("id"))
        )

        serializer = sr.ClickPerDaySerializer(q, many=True)

        return Response(serializer.data, 200)

    @action(methods=["get"], detail=False, url_path="clicks-per-campaigns")
    def sum_click_per_offers(self, request, *args, **kwargs):

        q = Offer.objects.annotate(count=Count("offer_click")).filter(count__gt=0)
        serializer = sr.ClickPerOfferSerializer(q, many=True)

        return Response(serializer.data, 200)


@extend_schema_view(list=extend_schema(tags=["statistic"]))
class PieceStatisticViewSet(viewsets.GenericViewSet):
    queryset = Click.objects.all()

    @action(methods=["get"], detail=False)
    def count_click_per_interest_level(self, request, *args, **kwargs):

        result = Click.objects.values("interest_level").annotate(
            total=Count("interest_level")
        )
        serialiazer = sr.InterestLevelCountSerializer(result, many=True)

        return Response(serialiazer.data, 200)
