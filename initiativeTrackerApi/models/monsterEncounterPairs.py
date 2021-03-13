from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .monster import Monster

class Monsterencounterpair(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    monsterId = models.ForeignKey(Monster, on_delete=models.CASCADE)
    initiative = models.IntegerField()
    currentHealth = models.IntegerField(null=True)
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField(default=0)