from rest_framework import routers

from .views import SubscriberViewSet

router = routers.SimpleRouter()
router.register('subscribers', SubscriberViewSet)

urlpatterns = router.urls
