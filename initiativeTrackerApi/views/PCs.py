from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import PlayerCharacter, Campaign

class PlayerSerealizer(serializers.ModelSerializer):

    class Meta:
        model =  PlayerCharacter
        fields = ('id', 'name', 'level', 'AC', 'maxHP', 'initiativeBonus',
        'strengthStat', 'dexterityStat', 'constitutionStat', 'intelligenceStat', 'wisdomStat',
        'charismaStat', 'speed', 'characterClass', 'strength_mod', 'dexterity_mod',
        'constitution_mod', 'intelligence_mod', 'wisdom_mod', 'charisma_mod', 'strength_ST',
        'dexterity_ST', 'constitution_ST', 'intelligence_ST', 'wisdom_ST', 'charisma_ST', 'campaign', 'spellSave_DC'
        )
        depth = 1

class PlayerCharacterView(ViewSet):

    def list(self, request):
        players = PlayerCharacter.objects.filter(user=request.auth.user)

        campaign = self.request.query_params.get('campaign', None)

        if campaign is not None:
            players = players.filter(campaign_id=campaign)

        json_data = PlayerSerealizer(players, many=True, context={'request': request})

        return Response(json_data.data)

    def retrieve(self, request, pk=None):
        player = PlayerCharacter.objects.get(pk=pk)
        json_data = PlayerSerealizer(player,context={'request': request})

        return Response(json_data.data)


    def destroy(self, request, pk=None):
        try:
            player = PlayerCharacter.objects.get(pk=pk)

            if player.user != request.auth.user:
                return Response({}, status=status.HTTP_401_UNAUTHORIZED)
            player.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except PlayerCharacter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        player = PlayerCharacter.objects.get(pk=pk)
        player.name = request.data["name"]
        player.level = request.data["level"]
        player.AC = request.data["AC"]
        player.maxHP = request.data["maxHP"]
        player.initiativeBonus = request.data["initiativeBonus"]
        player.strengthStat = request.data["strengthStat"]
        player.dexterityStat = request.data["dexterityStat"]
        player.constitutionStat = request.data["constitutionStat"]
        player.intelligenceStat = request.data["intelligenceStat"]
        player.wisdomStat = request.data["wisdomStat"]
        player.charismaStat = request.data["charismaStat"]
        player.speed = request.data["speed"]
        player.characterClass = request.data["characterClass"]

        player.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        player = PlayerCharacter()
        player.user = request.auth.user
        player.name = request.data["name"]
        player.level = request.data["level"]
        player.AC = request.data["AC"]
        player.maxHP = request.data["maxHP"]
        player.initiativeBonus = request.data["initiativeBonus"]
        player.strengthStat = request.data["strengthStat"]
        player.dexterityStat = request.data["dexterityStat"]
        player.constitutionStat = request.data["constitutionStat"]
        player.intelligenceStat = request.data["intelligenceStat"]
        player.wisdomStat = request.data["wisdomStat"]
        player.charismaStat = request.data["charismaStat"]
        player.speed = request.data["speed"]
        player.characterClass = request.data["characterClass"]

        campaign = Campaign.objects.get(pk=request.data["campaignId"])
        player.campaign = campaign

        try:
            player.save()
            serializer = PlayerSerealizer(player, context= {'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
