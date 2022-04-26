from postmarker.core import PostmarkClient, ClientError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView

from .serializers import ContactFormSerializer
from .utils import send_contact_form_email


class SubmitContactFormView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ContactFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            send_contact_form_email(serializer.data)
        except ClientError:
            return Response({'success': False}, status=HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'success': True}, status=HTTP_200_OK)
