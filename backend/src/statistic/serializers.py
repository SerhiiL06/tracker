from rest_framework import serializers


class ClickPerDaySerializer(serializers.Serializer):
    date = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_date(self, obj):
        return obj["date"].date()


class InterestLevelCountSerializer(serializers.Serializer):
    interest_level = serializers.CharField()
    total = serializers.IntegerField()
