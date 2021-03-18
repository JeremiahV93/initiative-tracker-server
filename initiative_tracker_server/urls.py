
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from initiativeTrackerApi.views import login_user, register_user, apiScrapper
from initiativeTrackerApi.views import Encounters, PlayerCharacterView, MonsterView, EncounterPairViews

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'encounters', Encounters, 'encounter')
router.register(r'players', PlayerCharacterView, 'player')
router.register(r'monsters', MonsterView, 'monster')
router.register(r'encounterpairs', EncounterPairViews, 'encounterpair')



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    # path('scrap', apiScrapper),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
