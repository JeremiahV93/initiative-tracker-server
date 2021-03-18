from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Encounter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = models.CharField(max_length=75)
    roomcode = models.CharField( unique=True ,max_length=4)
    archive = models.BooleanField(default=False)

    # def generate_room_codes(length):
    #     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #     code_list = [''.join(i) for i in product(chars, repeat=length)]
    #     return code_list

    # @property
    # def roomcode(self):
    #      roomcode = self.generate_room_codes(4)
    #      return roomcode
