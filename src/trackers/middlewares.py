import re

from .common import ClickAction, Interests
from .models import Click, Lead


class TrackerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        action_type = self.get_action_type(request)

        if action_type is None:
            return response

        lead_instance = self.get_or_create_lead(request)

        interest_level_click = self.get_interest_level(action_type)

        Click.objects.create(
            lead=lead_instance,
            interest_level=interest_level_click,
            action=action_type,
        )

        return response

    @classmethod
    def get_or_create_lead(cls, request):

        user_ip = request.META["REMOTE_ADDR"]
        agent = request.META["HTTP_USER_AGENT"]

        lead, _ = Lead.objects.get_or_create(
            ip_address=user_ip, defaults={"agent": agent}
        )

        return lead

    @classmethod
    def get_action_type(cls, request):

        action_type = None
        path = request.path

        if re.fullmatch(r"\/campaigns\/", path):
            action_type = ClickAction.CAMPAIGN_LIST

        elif re.fullmatch(r"\/campaigns\/\w+", path):
            action_type = ClickAction.CAMPAIGN_DETAIL

        elif re.fullmatch(r"\/offers\/", path):
            action_type = ClickAction.OFFER_LIST

        elif re.fullmatch(r"\/offers\/\w+", path):
            action_type = ClickAction.OFFER_DETAIL

        return action_type

    @classmethod
    def get_interest_level(cls, action: ClickAction):

        levels = {
            ClickAction.CAMPAIGN_LIST: Interests.LOW,
            ClickAction.CAMPAIGN_DETAIL: Interests.MIDDLE,
            ClickAction.OFFER_LIST: Interests.MIDDLE,
            ClickAction.OFFER_DETAIL: Interests.HIGH,
        }

        return levels.get(action)
