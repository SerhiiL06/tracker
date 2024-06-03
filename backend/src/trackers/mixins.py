import re

from django.urls import resolve

from .common import ClickAction, Interests
from .models import Lead


class TrackMiddlewareMixin:
    def get_or_create_lead(cls, request):

        try:
            user_ip = request.META["REMOTE_ADDR"]
            user_agent = request.META["HTTP_USER_AGENT"]

        except KeyError as _:
            return None

        os_pattern = re.compile(r"\((.*?)\)")
        agent_pattern = re.compile(r"\b(?:\w+\/)\d+\.\d+\b")

        agent = agent_pattern.search(user_agent)
        os = os_pattern.search(user_agent)

        lead, _ = Lead.objects.get_or_create(
            ip_address=user_ip, defaults={"agent": agent.group(), "os": os.group()}
        )

        return lead

    def get_action_type(cls, request):

        url_name = resolve(request.path).url_name
        action_types = {
            "campaigns-list": ClickAction.CAMPAIGN_LIST,
            "campaigns-detail": ClickAction.CAMPAIGN_DETAIL,
            "offers-list": ClickAction.OFFER_LIST,
            "offers-detail": ClickAction.OFFER_DETAIL,
        }

        return action_types.get(url_name, None)

    def get_interest_level(cls, action: ClickAction):

        levels = {
            ClickAction.CAMPAIGN_LIST: Interests.LOW,
            ClickAction.CAMPAIGN_DETAIL: Interests.MIDDLE,
            ClickAction.OFFER_LIST: Interests.MIDDLE,
            ClickAction.OFFER_DETAIL: Interests.HIGH,
        }

        return levels.get(action)
