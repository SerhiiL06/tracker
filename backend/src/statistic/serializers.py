from rest_framework import serializers


class ClickPerDaySerializer(serializers.Serializer):
    date = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_date(self, obj):
        return obj["date"].date()


class ClickPerOfferSerializer(serializers.Serializer):
    offer = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_offer(self, obj):
        return obj.title


class InterestLevelCountSerializer(serializers.Serializer):
    interest_level = serializers.CharField()
    total = serializers.IntegerField()
