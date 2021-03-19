from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .monster import Monster
from .encounter import Encounter

class Monsterencounterpair(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    monsterId = models.ForeignKey(Monster, on_delete=models.CASCADE)
    encounterId = models.ForeignKey(Encounter, on_delete=models.CASCADE, default=1  )
    initiative = models.IntegerField()
    currentHealth = models.IntegerField()
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField(default=0)
