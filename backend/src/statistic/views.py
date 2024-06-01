from rest_framework import viewsets
from rest_framework.decorators import action


class StatisticViewSet(viewsets.GenericViewSet):
    @action(methods=["get"], detail=False)
    def something(self): ...
