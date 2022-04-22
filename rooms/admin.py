from django.contrib import admin
from .models import Room, Deck

class RoomAdmin(admin.ModelAdmin):
    fields = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    list_display = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    readonly_fields = ['room_code']

admin.site.register(Room, RoomAdmin)

class DeckAdmin(admin.ModelAdmin):
    fields = ['app_user', 'suit', 'card_no', 'priority', 'point', 'img', 'is_trump']
    list_display = ['app_user', 'suit', 'card_no', 'priority', 'point', 'img', 'is_trump']

admin.site.register(Deck, DeckAdmin)