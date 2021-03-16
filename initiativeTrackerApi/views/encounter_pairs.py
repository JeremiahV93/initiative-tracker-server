from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Monsterencounterpair, Playerencounterpair, Monster, PlayerCharacter
from .monsters import MonsterSerialzer
from .PCs import PlayerSerealizer

class MonsterPairSerializer(serializers.ModelSerializer):

    class Meta():
        model = Monsterencounterpair
        fields = ('id', 'initiative', 'monsterId', 'currentHealth', 'concentration', 'temporaryHealth')
        depth = 1

class PlayerPairSerializer(serializers.ModelSerializer):

    class Meta():
        model = Playerencounterpair
        fields = ('id', 'initiative', 'characterId', 'currentHealth', 'concentration', 'temporaryHealth')
        depth = 1

# class AllPairsSerializer(serializers.Serializer):


class EncounterPairViews(ViewSet):
    def list(self, request, pk=None):

        all_monsters = Monsterencounterpair.objects.all()
        all_players = Playerencounterpair.objects.all()


        encounter_id = self.request.query_params.get('encounterId', None)

        if encounter_id is not None:
            all_monsters = all_monsters.filter(encounterId=encounter_id)
            all_players = all_players.filter(encounterId=encounter_id)


        all_monsters = MonsterPairSerializer(all_monsters, many=True, context={'request': request})
        all_players = PlayerPairSerializer(all_players, many=True, context={"request": request})

        empty = {}

        empty["monsters"] = all_monsters.data
        empty["players"] = all_players.data
        return Response(empty)
