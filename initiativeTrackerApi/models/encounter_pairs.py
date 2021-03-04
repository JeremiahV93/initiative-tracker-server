from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .monster import Monster
from .player_character import PlayerCharacter

class Encounterpair(self):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    characterId = models.ForeignKey(Monster, PlayerCharacter on_delete=models,CASCADE)
    initiative = models.IntegerField()
    currentHealth = models.IntegerField()
    concentration = models.BooleanField(default=False)
    temporaryHealth = models.IntegerField()
