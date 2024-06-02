from .mixins import TrackMiddlewareMixin
from .models import Click, Offer
from .common import ClickAction
from django.urls import resolve


class TrackerMiddleware(TrackMiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        action_type = self.get_action_type(request)

        if action_type is None:
            return response

        lead_instance = self.get_or_create_lead(request)

        if lead_instance is None:
            return response

        interest_level_click = self.get_interest_level(action_type)

        offer = None

        slug = resolve(request.path).kwargs.get("slug", None)

        if action_type == ClickAction.OFFER_DETAIL:
            offer = Offer.objects.get(slug=slug)

        Click.objects.create(
            lead=lead_instance,
            interest_level=interest_level_click,
            action=action_type,
            offer=offer,
        )

        return response
