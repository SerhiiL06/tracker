from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("campaigns", views.CampaignViewSet)
router.register("offers", views.OfferViewSet)
router.register("leads", views.LeadViewSet)

urlpatterns = []


urlpatterns += router.urls
