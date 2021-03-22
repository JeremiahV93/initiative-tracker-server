from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from initiativeTrackerApi.models import Campaign

class CampaignSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'archive')

class Campaigns(ViewSet):

# get all active Campaign
    def list(self, request):
        campaigns = Campaign.objects.all().filter(user=request.auth.user, archive=False)

        archive = self.request.query_params.get('archive', None)

        if archive is not None:
            campaigns = campaigns.filter(archive=archive)

        json_data = CampaignSerealizer(campaigns, many=True, context={'request': request})

        return Response(json_data.data)

    def retrieve(self, request, pk=None):

        campaign = Campaign.objects.get(pk=pk)
        seralizer = CampaignSerealizer(campaign, many=False, context={'request':request})

        return Response(seralizer.data)

    def destroy(self, request, pk=None):
        try:
            campaign = Campaign.objects.get(pk=pk)
            campaign.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Campaign.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        campaign = Campaign.objects.get(pk=pk)
        campaign.name = request.data["name"]

        campaign.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def create(self, request):
        campaign = Campaign()
        campaign.name = request.data["name"]
        campaign.user = request.auth.user

        try:
            campaign.save()
            serializer = CampaignSerealizer(campaign, context= {'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
