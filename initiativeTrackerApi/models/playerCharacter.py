from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .ability_score_modifier import modifier_clac
from .prof_bonus import prof_bonus


class PlayerCharacter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    level = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(20)],)
    AC = models.IntegerField()
    maxHP = models.IntegerField()
    initiativeBonus = models.IntegerField()
    strengthStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],) 
    dexterityStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    constitutionStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    intelligenceStat = models.IntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(30)],)
    wisdomStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    charismaStat = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(30)],)
    speed = models.CharField(max_length=50)
    alive = models.BooleanField(default=True)

    class_choices = (
        ('bab', 'Barbarian'),
        ('bad', 'Bard'),
        ('cle', 'Cleric'),
        ('dru', 'Druid'),
        ('fig', 'Fighter'),
        ('mon', 'Monk'),
        ('pal', 'Paladin'),
        ('ran', 'Ranger'),
        ('rog', 'Rogue'),
        ('sor', 'Sorcerer'),
        ('war', 'Warlock'),
        ('wiz', 'Wizard'),
    )
    characterClass = models.CharField(max_length=3, choices=class_choices, default=None)


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

    @property
    def strength_ST(self):
        strength_ST = None
        if self.characterClass in ['bab', 'fig', 'mon', 'rag']:
            strength_ST = prof_bonus(self.level)  + self.strength_mod()
        else:
            strength_ST = self.strength_mod()
        return strength_ST

    @property
    def dexterity_ST(self):
        dexterity_ST = None
        if self.characterClass in ['bad', 'rog', 'mon', 'ran']:
            dexterity_ST = prof_bonus(self.level)  + self.dexterity_mod()
        else:
            dexterity_ST = self.dexterity_mod()
        return dexterity_ST

    @property
    def constitution_ST(self):
        constitution_ST = None
        if self.characterClass in ['bab', 'fig', 'sor']:
            constitution_ST = prof_bonus(self.level)  + self.constitution_mod()
        else:
            constitution_ST = self.constitution_mod()
        return constitution_ST

    @property
    def intelligence_ST(self):
        intelligence_ST = None
        if self.characterClass in ['dru', 'rog', 'wiz']:
            intelligence_ST = prof_bonus(self.level)  + self.intelligence_mod()
        else:
            intelligence_ST = self.intelligence_mod()
        return intelligence_ST

    @property
    def wisdom_ST(self):
        wisdom_ST = None
        if self.characterClass in ['cle', 'dru', 'pal']:
            wisdom_ST = prof_bonus(self.level)  + self.wisdom_mod()
        else:
            wisdom_ST = self.wisdom_mod()
        return wisdom_ST

    @property
    def charisma_ST(self):
        charisma_ST = None
        if self.characterClass in ['bad', 'cle', 'pal', 'sor', 'war']:
            charisma_ST = prof_bonus(self.level)  + self.charisma_mod()
        else:
            charisma_ST = self.charisma_mod()
        return charisma_ST