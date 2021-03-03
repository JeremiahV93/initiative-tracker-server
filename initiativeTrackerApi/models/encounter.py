from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Encounter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(max_length=75)
    roomcode = models.CharField(max_length=4)
    archive = models.BooleanField(default=False)
