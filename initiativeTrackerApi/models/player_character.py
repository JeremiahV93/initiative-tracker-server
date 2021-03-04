from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .ability_score_modifier import modifier_clac


class PlayerCharacter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    level = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    AC = models.IntegerField()
    maxHP = models.IntegerField()
    initiativeBonus = models.IntegerField()
    characterClass = models.CharField(max_length=50)
    strengthStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],) 
    dexterityStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    constitutionStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    intelligenceStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    wisdomStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    charismaStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    speed = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("player character")
        verbose_name_plural =("player characters")

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
