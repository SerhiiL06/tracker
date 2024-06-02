from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path


urlpatterns = [
    path("", views.StatisticViewSet.as_view({"get": "sum_clicks_per_day"})),
    path(
        "clicks-per-camp/",
        views.StatisticViewSet.as_view({"get": "sum_click_per_campaigns"}),
    ),
    path(
        "click-per-interest-level/",
        views.PieceStatisticViewSet.as_view({"get": "count_click_per_interest_level"}),
    ),
]
