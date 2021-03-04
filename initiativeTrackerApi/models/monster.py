from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .ability_score_modifyer import modifier_clac


class Monster(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE, )
    name = models.CharField(max_length=50)
    challengeRating = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    AC = models.IntegerField()
    maxHP = models.IntegerField()
    initiativeBonus = models.IntegerField()
    monsterType = models.CharField(max_length=50)
    damageResistance = models.TextField()
    damageImmunity = models.TextField()
    conditionImmunity = models.TextField()
    speed = models.CharField(max_length=50)
    spellcaster = models.BooleanField()

    strengthStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],) 
    dexterityStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    constitutionStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    intelligenceStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    wisdomStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    charismaStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    


    Tiny = "t"
    Small = "s"
    Medium = "m"
    Large = "l"
    Huge = "h"
    Gargantuan = "g"
    size_choices = [
        (Tiny, "tiny")
        (Small,"small")
        (Medium, "medium")
        (Large, "large")
        (Huge, "huge")
        (Gargantuan, "gargantuan")
    ]
    size = models.CharField(max_length=1, choices=size_choices, default=Medium)

    @property
    def strength_mod(self):
        str_st = modifier_clac(self.strengthStat)
        return str_st
 
    @property
    def dexterity_mod(self):
        dex_st = modifier_clac(self.dexterityStat)
        return dex_st

    @property
    def constitution_mod(self):
        con_st = modifier_clac(self.constitutionStat)
        return con_st

    @property
    def intelligence_mod(self):
        int_st = modifier_clac(self.intelligenceStat)
        return int_st

    @property
    def wisdom_mod(self):
        wis_st = modifier_clac(self.wisdomStat)
        return wis_st

    @property
    def charisma_mod(self):
        cha_st = modifier_clac(self.charismaStat)
        return cha_st
