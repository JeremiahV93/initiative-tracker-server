from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .ability_score_modifier import modifier_clac


class Monster(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, )
    name = models.CharField(max_length=50)
    challengeRating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)],)
    AC = models.IntegerField()
    maxHP = models.IntegerField()
    initiativeBonus = models.IntegerField()
    monsterType = models.CharField(max_length=50)
    damageResistance = models.TextField(default="none")
    damageImmunity = models.TextField(default="none")
    conditionImmunity = models.TextField(default="none")
    speed = models.CharField(max_length=50)
    spellcaster = models.BooleanField(default=False)

    strengthStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    dexterityStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    constitutionStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    intelligenceStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    wisdomStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    charismaStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)

    strength_savingthrow = models.IntegerField(default=0)
    dexterity_savingthrow = models.IntegerField(default=0)
    constitution_savingthrow = models.IntegerField(default=0)
    intelligence_savingthrow = models.IntegerField(default=0)
    wisdom_savingthrow = models.IntegerField(default=0)
    charisma_savingthrow = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("monster")
        verbose_name_plural = ("monsters")

    SIZE_CHOICES = ( 
        ("tiny", "tiny"),
        ("small", "small"),
        ("medium", "medium"),
        ("large", "large"),
        ("huge", "huge"),
        ("gargantuan", "gargantuan"),
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')

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
