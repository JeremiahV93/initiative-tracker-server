from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .playerCharacter import PlayerCharacter

class Encounterpair(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    characterId = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE)
    initiative = models.IntegerField()
    currentHealth = models.IntegerField()
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField()