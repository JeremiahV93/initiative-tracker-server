import requests
import json

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "initiative_tracker_server.settings")
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# from django.conf import settings
# settings.configure()

from .models import Monster

def get_api_data():
    url = 'https://www.dnd5eapi.co/api/monsters'
    res = requests.get(url)
    # what returns is a byte variable 
    # res_type = type(res.content)
    # this decodes it into json
    res = json.loads(res.content)

    
    # base url to combine witht he URL in the monsters results
    monster_url = 'https://www.dnd5eapi.co'

    monster_res = requests.get('https://www.dnd5eapi.co/api/monsters/zombie')
    monster_res =json.loads(monster_res.content)


    # for monster in res['results']:
    #     each_url = monster['url']
    #     new_url = f'{monster_url}{each_url}'
    #     monster_res = requests.get(each_url)
    #     monster_res = json.loads(monster_res.content)
    monster_res['name']
    monster_res['challenge_rating']
    monster_res['armor_class']
    monster_res['hit_points']
    monster_res['type']
    damageResistance
    damageImmunity
    conditionImmunity
    speed



    monster_res['size']

    monster_res['strength']
    monster_res['dexterity']
    monster_res['constitution']
    monster_res['intelligence']
    monster_res['wisdom']
    monster_res['charisma']



    


    #     print(monster_res)

    
    # res['results'] stores all the monster object things
    print(monster_res['size'], monster_res['type'])

    return 'droplet_list'

get_api_data()
