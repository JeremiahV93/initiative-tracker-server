import urllib.request
from initiativeTrackerApi.models import Monster

with urllib.request.Request('https://www.dnd3eapi.co/api/monsters') as request:
    print(request)
