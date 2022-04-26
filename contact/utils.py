from django.conf import settings
from postmarker.core import PostmarkClient

TEMPLATE_ID = 25640733


def send_contact_form_email(data):
    postmark = PostmarkClient(server_token=settings.POSTMARK_API_TOKEN)
    postmark.emails.send_with_template(
        From=settings.POSTMARK_EMAIL_FROM,
        To=settings.POSTMARK_EMAIL_TO,
        TemplateId=TEMPLATE_ID,
        TemplateModel=data)
