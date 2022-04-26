from rest_framework import serializers

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    """Serialize a newsletter subscriber."""

    class Meta():
        model = Subscriber
        fields = ['email']
