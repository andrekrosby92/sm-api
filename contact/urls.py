from django.urls import path

from .views import SubmitContactFormView

urlpatterns = [
    path('submit-contact-form/', SubmitContactFormView.as_view()),
]
