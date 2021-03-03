from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator


class Playercharacter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    level = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    AC = models.IntegerField()
    maxHP = models.IntegerField()
    initiativeBonus = models.IntegerField()
    characterClass = models.CharField(max_length=50)
    strengthStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)  
    dexterityStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    constitutionStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(20)],)
    intelligenceStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(20)],)
    wisdomStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    charismaStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    speed = models.CharField(max_length=50)
