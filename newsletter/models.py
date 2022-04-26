import uuid
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
