import requests
import json

from initiativeTrackerApi.models import Monster
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def apiScrapper(request):
    url = 'https://www.dnd5eapi.co/api/monsters'
    res = requests.get(url)
    # what returns is a byte variable 
    # this decodes it into json
    res = json.loads(res.content)

    # base url to combine witht he URL in the monsters results
    monster_url = 'https://www.dnd5eapi.co'

    for monster in res['results']:
        each_url = monster['url']
        new_url = f'{monster_url}{each_url}'
        monster_res = requests.get(new_url)
        monster_res = json.loads(monster_res.content)
    
        user = User.objects.get(pk=1)

        monster = Monster()
        monster.user = user
        monster.name = monster_res['name']
        monster.challengeRating = monster_res['challenge_rating']
        monster.AC = monster_res['armor_class']
        monster.maxHP = monster_res['hit_points']
        monster.monsterType = monster_res['type']

        speed = ''
        for speed_type, speed_distance in monster_res['speed'].items():
            speed += f'{speed_type} {speed_distance}, '
        monster.speed = speed[:-2]

        damageImmunity = ''
        for each in monster_res['damage_immunities']:
            damageImmunity += f'{each}, '
        monster.damageImmunity = damageImmunity[:-2]

        damageResistances = ''
        for each in monster_res['damage_resistances']:
            damageResistances += f'{each}, '
        monster.damageResistance = damageResistances[:-2]

        conditionImmunity = ''
        for eachObj in monster_res['condition_immunities']:
            conditionImmunity += f'{eachObj["index"]}, '
        monster.conditionImmunity = conditionImmunity[:-2]

        for eachObj in monster_res['proficiencies']:
            if 'STR' in eachObj['proficiency']['name']:
                monster.strength_savingthrow = eachObj['value']
            if 'DEX' in eachObj['proficiency']['name']:
               monster.dexterity_savingthrow = eachObj['value']
            if 'CON' in eachObj['proficiency']['name']:
                monster.constitution_savingthrow = eachObj['value']
            if 'WIS' in eachObj['proficiency']['name']:
                monster.wisdom_savingthrow = eachObj['value']
            if 'INT' in eachObj['proficiency']['name']:
                monster.intelligence_savingthrow = eachObj['value']
            if 'CHA' in eachObj['proficiency']['name']:
                monster.charisma_savingthrow = eachObj['value']

        monster.size = monster_res['size']
        monster.strengthStat = monster_res['strength']
        monster.dexterityStat = monster_res['dexterity']
        monster.constitutionStat = monster_res['constitution']
        monster.intelligenceStat = monster_res['intelligence']
        monster.wisdomStat = monster_res['wisdom']
        monster.charismaStat = monster_res['charisma']

        monster.save()

    return HttpResponse(res, content_type='application/json')
