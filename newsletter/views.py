from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
