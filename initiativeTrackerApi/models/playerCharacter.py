from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from .ability_score_modifier import modifier_clac
from .prof_bonus import prof_bonus
from .campaign import Campaign



class PlayerCharacter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=CASCADE)
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
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    )
    characterClass = models.CharField(max_length=9, choices=class_choices, default=None)


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

    def strength_ST(self):
        strength_st = None
        if self.characterClass in ['Barbarian', 'Fighter', 'Monk', 'Ranger']:
            strength_st = prof_bonus(self.level)  + self.strength_mod
        else:
            strength_st = self.strength_mod
        return strength_st

    @property
    def dexterity_ST(self):
        dexterity_st = None
        if self.characterClass in ['Bard', 'Rogue', 'Monk', 'Ranger']:
            dexterity_st = prof_bonus(self.level)  + self.dexterity_mod
        else:
            dexterity_st = self.dexterity_mod
        return dexterity_st

    @property
    def constitution_ST(self):
        constitution_st = None
        if self.characterClass in ['Barbarian', 'Fighter', 'Sorcerer']:
            constitution_st = prof_bonus(self.level)  + self.constitution_mod
        else:
            constitution_st = self.constitution_mod
        return constitution_st

    @property
    def intelligence_ST(self):
        intelligence_st = None
        if self.characterClass in ['Druid', 'Rogue', 'Wizard']:
            intelligence_st = prof_bonus(self.level)  + self.intelligence_mod
        else:
            intelligence_st = self.intelligence_mod
        return intelligence_st

    @property
    def wisdom_ST(self):
        wisdom_st = None
        if self.characterClass in ['Cleric', 'Druid', 'Paladin', 'Warlock', 'Wizard']:
            wisdom_st = prof_bonus(self.level)  + self.wisdom_mod
        else:
            wisdom_st = self.wisdom_mod
        return wisdom_st

    @property
    def charisma_ST(self):
        charisma_st = None
        if self.characterClass in ['Bard', 'Cleric', 'Paladin', 'Sorcerer', 'Warlock']:
            charisma_st = prof_bonus(self.level)  + self.charisma_mod
        else:
            charisma_st = self.charisma_mod
        return charisma_st
