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


        """
        Get all Monster and Player encounter pairs
        """
        all_monsters = Monsterencounterpair.objects.all()
        all_players = Playerencounterpair.objects.all()


        encounter_id = self.request.query_params.get('encounterId', None)

        """
        api/encounterpairs?encounterId?X

        Filter for the just the Monsters and Player assigned to the encounter Id provided
        """

        if encounter_id is not None:
            all_monsters = all_monsters.filter(encounterId=encounter_id)
            all_players = all_players.filter(encounterId=encounter_id)

        """
        Serealize each Monster/Player
        """


        all_monsters = MonsterPairSerializer(all_monsters, many=True, context={'request': request})
        all_players = PlayerPairSerializer(all_players, many=True, context={"request": request})

        all_creatures = {}

        all_creatures["monsters"] = all_monsters.data
        all_creatures["players"] = all_players.data
        return Response(all_creatures)

    def create(self, request):
        if request.data["monsterId"] is not None:
            monster_pair = Monsterencounterpair()
            monster_pair.user = request.auth.user
            monster_pair.monsterId = request.data["monsterId"]
            monster_pair.encounterId = request.data["encounterId"]
            monster_pair.initiative = request.data["initiative"]

            monster = Monster.objects.get(pk=request.data["monsterId"])
            monster_pair.currentHealth = monster.maxHP

            monster_pair.concentration = False
            monster_pair.temporaryHealth = 0

            try:
                monster_pair.save()
                serializer = MonsterPairSerializer(monster_pair,  context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        else:
            player_pair = Playerencounterpair()
            player_pair.user = request.auth.user
            player_pair.characterId = request.data["characterId"]
            player_pair.encounterId = request.data["encounterId"]
            player_pair.initiative = request.data["initiative"]

            player = PlayerCharacter.objects.get(pk=request.data["characterId"])
            player_pair.currentHealth = player.maxHP

            player_pair.concentration = False
            player_pair.temporaryHealth = 0

            try:
                player_pair.save()
                serializer = PlayerPairSerializer(player_pair,  context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request):
        if request.data["monsterId"] is not None:
            try:
                monster_pair = Monsterencounterpair.objects.get(pk=request.data["monsterId"])
                monster_pair.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except Monsterencounterpair.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        else:
            try:
                player_pair = Playerencounterpair.objects.get(pk=request.data["characterId"])
                player_pair.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except Playerencounterpair.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request):
        if request.data["monsterId"] is not None:
            monster_pair = Monsterencounterpair.objects.get(pk=request.data["monsterId"])
            monster_pair.encounterId = request.data["encounterId"]
            monster_pair.initiative = request.data["initiative"]
            monster_pair.currentHealth = request.data["currentHealth"]
            monster_pair.concentration = request.data["concentration"]
            monster_pair.temporaryHealth = request.data["temporaryHealth"]

            try:
                monster_pair.save()
                serializer = MonsterPairSerializer(monster_pair,  context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        else:
            player_pair = Playerencounterpair.objects.get(pk=request.data["characterId"])
            player_pair.encounterId = request.data["encounterId"]
            player_pair.initiative = request.data["initiative"]
            player_pair.currentHealth = request.data["currentHealth"]
            player_pair.concentration = request.data["concentration"]
            player_pair.temporaryHealth = request.data["temporaryHealth"]

            try:
                player_pair.save()
                serializer = PlayerPairSerializer(player_pair,  context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
