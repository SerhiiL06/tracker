from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("campaigns", views.CampaignViewSet, basename="campaigns")
router.register("offers", views.OfferViewSet, basename="offers")
router.register("leads", views.LeadViewSet, basename="leads")
router.register("clicks", views.ClickViewSet)

urlpatterns = []


urlpatterns += router.urls
