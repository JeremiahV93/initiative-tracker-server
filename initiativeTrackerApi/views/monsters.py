from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Monster

class MonsterSerialzer(serializers.ModelSerializer):

    class Meta:
        model =  Monster
        fields = ('id', 'user', 'name', 'challengeRating', 'AC', 'maxHP', 'initiativeBonus',
        'monsterType', 'damageResistance', 'damageImmunity', 'conditionImmunity', 
        'speed', 'spellcaster', 'strengthStat', 'dexterityStat' , 'constitutionStat',
         'intelligenceStat',
        'wisdomStat', 'charismaStat', 'strength_savingthrow', 'dexterity_savingthrow',
         'constitution_savingthrow',
        'intelligence_savingthrow', 'wisdom_savingthrow', 'charisma_savingthrow', 'size',
        'strength_mod', 'dexterity_mod', 'constitution_mod', 'intelligence_mod',
         'wisdom_mod', 'charisma_mod')


class MonsterView(ViewSet):

    def list(self, request):
        monsters = Monster.objects.all()

        challenge_rating = self.request.query_params.get('challengeRating', None)
        monster_type = self.request.query_params.get('monsterType', None)
        active_user = self.request.query_params.get('activeUser', None)
        pages = self.request.query_params.get('pages', None)


        if challenge_rating is not None:
            monsters = monsters.filter(challengeRating=challenge_rating)
        if monster_type is not None:
            monsters = monsters.filter(monsterType=monster_type)
        if active_user is not None:
            monsters = monsters.filter(user=active_user)
        if pages is not None:
            pages = int(pages)
            max_pages = pages + 25
            monsters = monsters.filter(pk__gt=pages,pk__lte=max_pages)
        

        json_data = MonsterSerialzer(monsters, many=True, context={'request': request})

        return Response(json_data.data)

    def retrieve(self, request, pk=None):
        monster = Monster.objects.get(pk=pk)
        json_data = MonsterSerialzer(monster,context={'request': request})

        return Response(json_data.data)


    def destroy(self, request, pk=None):
        try:
            monster = Monster.objects.get(pk=pk)

            if monster.user != request.auth.user:
                return Response({}, status=status.HTTP_401_UNAUTHORIZED)

            monster.delete()

            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except Monster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        monster = Monster.objects.get(pk=pk)
        monster.name = request.data["name"]
        monster.challengeRating = request.data["challengeRating"]
        monster.AC = request.data["AC"]
        monster.maxHP = request.data["maxHP"]
        monster.initiativeBonus = request.data["initiativeBonus"]
        monster.strengthStat = request.data["strengthStat"]
        monster.dexterityStat = request.data["dexterityStat"]
        monster.constitutionStat = request.data["constitutionStat"]
        monster.intelligenceStat = request.data["intelligenceStat"]
        monster.wisdomStat = request.data["wisdomStat"]
        monster.charismaStat = request.data["charismaStat"]
        monster.speed = request.data["speed"]
        monster.monsterType = request.data["monsterType"]
        monster.size = request.data["size"]
        monster.damageResistance = request.data["damageResistance"]
        monster.damageImmunity = request.data["damageImmunity"]
        monster.conditionImmunity = request.data["conditionImmunity"]
        monster.spellcaster = request.data["spellcaster"]



        monster.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
   
    def create(self, request):
        monster = Monster()
        monster.user = request.auth.user
        monster.name = request.data["name"]
        monster.challengeRating = request.data["challengeRating"]
        monster.AC = request.data["AC"]
        monster.maxHP = request.data["maxHP"]
        monster.initiativeBonus = request.data["initiativeBonus"]
        monster.strengthStat = request.data["strengthStat"]
        monster.dexterityStat = request.data["dexterityStat"]
        monster.constitutionStat = request.data["constitutionStat"]
        monster.intelligenceStat = request.data["intelligenceStat"]
        monster.wisdomStat = request.data["wisdomStat"]
        monster.charismaStat = request.data["charismaStat"]
        monster.speed = request.data["speed"]
        monster.size = request.data["size"]
        monster.monsterType = request.data["monsterType"]
        monster.damageResistance = request.data["damageResistance"]
        monster.damageImmunity = request.data["damageImmunity"]
        monster.conditionImmunity = request.data["conditionImmunity"]

        try:
            monster.save()
            serializer = MonsterSerialzer(monster, context= {'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
