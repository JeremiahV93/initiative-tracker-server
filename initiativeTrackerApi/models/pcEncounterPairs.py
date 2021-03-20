from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .playerCharacter import PlayerCharacter
from .encounter import Encounter

class Playerencounterpair(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    characterId = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE)
    encounterId = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    initiative = models.IntegerField()
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField(default=0)
    currentHealth = models.IntegerField(null=True)
