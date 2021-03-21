from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Monsterencounterpair, Monster, Encounter
from .monsters import MonsterSerialzer

class MonsterPairSerializer(serializers.ModelSerializer):

    class Meta():
        model = Monsterencounterpair
        fields = ('id', 'initiative', 'monsterId', 'currentHealth', 'concentration', 'temporaryHealth')
        depth = 1

class MonsterPairViews(ViewSet):

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

    def update(self, request, pk=None):
        monster_pair = Monsterencounterpair.objects.get(pk=pk)
        monster_pair.initiative = request.data["initiative"]
        monster_pair.currentHealth = request.data["currentHealth"]
        monster_pair.concentration = request.data["concentration"]

        try:
            monster_pair.save()
            serializer = MonsterPairSerializer(monster_pair,  context= {'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
