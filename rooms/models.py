from django.db import models
import secrets

#importing user form django admin
from django.contrib.auth.models import User

from registration.models import AppUser



class Room(models.Model):
    person_1 = models.OneToOneField(AppUser, on_delete=models.PROTECT, related_name='person_1')
    person_2 = models.OneToOneField(AppUser, on_delete=models.PROTECT, related_name='person_2', null=True, blank=True)
    person_3 = models.OneToOneField(AppUser, on_delete=models.PROTECT, related_name='person_3', null=True, blank=True)
    person_4 = models.OneToOneField(AppUser, on_delete=models.PROTECT, related_name='person_4', null=True, blank=True)
    room_code = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return str(self.id)

