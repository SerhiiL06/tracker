from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path("", views.StatisticViewSet.as_view({"get": "sum_clicks_per_day"})),
    path(
        "clicks-per-offer/",
        views.StatisticViewSet.as_view({"get": "sum_click_per_offers"}),
    ),
    path(
        "click-per-interest-level/",
        views.PieceStatisticViewSet.as_view({"get": "count_click_per_interest_level"}),
    ),
]
