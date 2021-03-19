from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Campaign(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(null=False, max_length=75)
    archive = models.BooleanField(default=False)
