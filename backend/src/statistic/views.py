from rest_framework import viewsets
from rest_framework.decorators import action
from src.trackers.models import Campaign, Click, Lead, Offer
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncDay
from .serializers import ClickPerDaySerializer, InterestLevelCountSerializer


class StatisticViewSet(viewsets.GenericViewSet):
    queryset = Click.objects.all()

    @action(methods=["get"], detail=False, url_path="clicks-per")
    def sum_clicks_per_day(self, request, *args, **kwargs):

        q = (
            Click.objects.annotate(date=TruncDay("click_on"))
            .values("date")
            .annotate(count=Count("id"))
        )

        serializer = ClickPerDaySerializer(q, many=True)

        return Response(serializer.data, 200)

    @action(methods=["get"], detail=False, url_path="leads-per")
    def sum_leads_per_day(self, request, *args, **kwargs):

        q = (
            Lead.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(count=Count("id"))
        )

        serializer = ClickPerDaySerializer(q, many=True)

        return Response(serializer.data, 200)

    @action(methods=["get"], detail=False, url_path="clicks-per-campaigns")
    def sum_click_per_campaigns(self, request, *args, **kwargs):

        q = Campaign.objects.select_related("camp_click").annotate(
            count=Count("camp_click")
        )

        for e in q:

            print(e.count)
        serializer = ClickPerDaySerializer(q, many=True)

        return Response(serializer.data, 200)


class PieceStatisticViewSet(viewsets.GenericViewSet):
    queryset = Click.objects.all()

    @action(methods=["get"], detail=False)
    def count_click_per_interest_level(self, request, *args, **kwargs):

        result = Click.objects.values("interest_level").annotate(
            total=Count("interest_level")
        )
        serialiazer = InterestLevelCountSerializer(result, many=True)

        return Response(serialiazer.data, 200)
