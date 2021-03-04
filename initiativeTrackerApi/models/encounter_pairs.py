from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .monster import Monster
from .player_character import PlayerCharacter

class Encounterpair(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    monsterId = models.ForeignKey(Monster,  on_delete=models.CASCADE, null=True)
    characterId = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, null=True)
    initiative = models.IntegerField()
    currentHealth = models.IntegerField()
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField()
