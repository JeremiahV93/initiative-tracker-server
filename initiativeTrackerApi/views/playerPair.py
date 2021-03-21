from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Playerencounterpair, PlayerCharacter, Encounter
from .PCs import PlayerSerealizer 

class PlayerPairSerializer(serializers.ModelSerializer):

    class Meta():
        model = Playerencounterpair
        fields = ('id', 'initiative', 'characterId', 'currentHealth', 'concentration', 'temporaryHealth')
        depth = 1

class PlayerPairViews(ViewSet):

    def update(self, request, pk=None):
        player_pair = Playerencounterpair.objects.get(pk=pk)
        player_pair.initiative = request.data["initiative"]
        player_pair.currentHealth = request.data["currentHealth"]
        player_pair.concentration = request.data["concentration"]

        try:
            player_pair.save()
            serializer = PlayerPairSerializer(player_pair,  context= {'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
