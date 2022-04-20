from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    fields = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    list_display = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    readonly_fields = ['room_code']

admin.site.register(Room, RoomAdmin)