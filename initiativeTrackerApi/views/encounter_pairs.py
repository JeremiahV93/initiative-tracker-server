from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action
from initiativeTrackerApi.models import Monsterencounterpair, Playerencounterpair, Monster, PlayerCharacter, Encounter
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
    @action(methods=['delete'], detail=False)
    def monster_delete(self,request):
        try:
            monster_pair = Monsterencounterpair.objects.get(pk=request.data["monsterId"])
            monster_pair.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Monsterencounterpair.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):


        """
        Get all Monster and Player encounter pairs
        """
        all_monsters = Monsterencounterpair.objects.all()
        all_players = Playerencounterpair.objects.all()

        encounter_id = self.request.query_params.get('encounterId', None) 

        """
        invalid token, seperate data call/URL that is somehow public?
        """
        if self.request.query_params.get('roomCode', None):
            roodCodeKey = self.request.query_params.get('roomCode', None)
            roomCode = Encounter.objects.get(pk=roomCodeKey)
            encounter_id = roomCode.pk


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
        if request.data["monsterId"] != '':
            monster_pair = Monsterencounterpair()
            monster_pair.user = request.auth.user

            encounter = Encounter.objects.get(pk=request.data["encounterId"])
            monster_pair.encounterId = encounter
            monster_pair.initiative = 0

            monster = Monster.objects.get(pk=request.data["monsterId"])
            monster_pair.monsterId = monster
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
            encounter = Encounter.objects.get(pk=request.data["encounterId"])
            player_pair.encounterId = encounter
            player_pair.initiative = 0

            player = PlayerCharacter.objects.get(pk=request.data["characterId"])
            player_pair.characterId = player
            player_pair.currentHealth = player.maxHP

            player_pair.concentration = False
            player_pair.temporaryHealth = 0

            try:
                player_pair.save()
                serializer = PlayerPairSerializer(player_pair,  context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if request.data["monster"] is True:
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
