from rest_framework import serializers


class ContactFormSerializer(serializers.Serializer):
    """Serialize a contact form."""
    company = serializers.CharField(allow_blank=True, required=False)
    email = serializers.EmailField()
    message = serializers.CharField()
    name = serializers.CharField()
    phone_number = serializers.CharField(allow_blank=True, required=False)
