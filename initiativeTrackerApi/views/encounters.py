# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.http import HttpResponseServerError
from rest_framework import status
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

    def retrieve(self, request, pk=None):

        encounter = Encounter.objects.get(pk=pk)
        seralizer = EncounterSerealizer(encounter, many=False, context={'request':request})

        return Response(seralizer.data)

    def destroy(self, request, pk=None):
        try:
            encounter = Encounter.objects.get(pk=pk)
            encounter.delete()

            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except Encounter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        encounter = Encounter.objects.get(pk=pk)
        encounter.name = request.data["name"]

        encounter.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
