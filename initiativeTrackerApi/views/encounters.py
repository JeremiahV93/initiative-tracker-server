# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from django.http import HttpResponseServerError
from rest_framework import status
# from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Encounter, Campaign
import string
import random

class EncounterSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = ('id', 'name', 'roomcode', 'archive', 'campaign')
        depth = 1

class Encounters(ViewSet):

# get all active encounters
    def list(self, request):
        encounters = Encounter.objects.all().filter(user=request.auth.user, archive=False)

        archive = self.request.query_params.get('archive', None)
        campaign = self.request.query_params.get('campaign', None)

        if archive is not None:
            encounters = encounters.filter(archive=archive)
        if campaign is not None:
            encounters = encounters.filter(campaign_id=campaign)

        json_data = EncounterSerealizer(encounters, many=True, context={'request': request})

        return Response(json_data.data)


    def retrieve(self, request, pk=None):

        encounter = Encounter.objects.get(pk=pk)
        seralizer = EncounterSerealizer(encounter, many=False, context={'request':request})

        return Response(seralizer.data)

    def destroy(self, request, pk=None):
        try:
            encounter = Encounter.objects.get(pk=pk)
            encounter.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Encounter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        encounter = Encounter.objects.get(pk=pk)
        encounter.name = request.data["name"]
        campaign = Campaign.objects.get(pk=request.data["campaignId"])
        encounter.campaign = campaign

        encounter.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        encounter = Encounter()
        encounter.name = request.data["name"]
        campaign = Campaign.objects.get(pk=request.data["campaignId"])
        encounter.campaign = campaign
        encounter.roomcode = ''.join(random.choices(string.ascii_uppercase, k=4))
        encounter.user = request.auth.user

        try:
            encounter.save()
            serializer = EncounterSerealizer(encounter, context= {'request': request})
            return Response(serializer.data)
        except ValidationError:
            encounter.roomcode = ''.join(random.choices(string.ascii_uppercase, k=4))
            try:
                encounter.save()
                serializer = EncounterSerealizer(encounter, context= {'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
