from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .campaign import Campaign

class Encounter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=CASCADE)
    name = models.CharField(null=False, max_length=75)
    roomcode = models.CharField(unique=True, max_length=4)
    archive = models.BooleanField(default=False)
