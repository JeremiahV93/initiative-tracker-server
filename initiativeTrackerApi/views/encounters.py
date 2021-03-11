# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.http import HttpResponseServerError
# from rest_framework import status
# from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Encounter

class EncounterSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
    
        fields = ('id', 'name', 'roomcode')

class Encounters(ViewSet):
    
# get all active encounters
    def list(self, request):
        encounters = Encounter.objects.get(user=request.auth.user, archive=False)

        json_data = EncounterSerealizer(encounters, many=True, context={'request': request})

        return Response(json_data.data)
