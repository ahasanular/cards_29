from django.contrib import admin
from .models import Room, Deck, Card

class RoomAdmin(admin.ModelAdmin):
    fields = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    list_display = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']
    readonly_fields = ['room_code']

admin.site.register(Room, RoomAdmin)

class DeckAdmin(admin.ModelAdmin):
    fields = ['suit', 'card_no', 'priority', 'point', 'img']
    list_display = ['suit', 'card_no', 'priority', 'point', 'img']

admin.site.register(Deck, DeckAdmin)

class CardAdmin(admin.ModelAdmin):
    fields = ['app_user', 'card']
    list_display = ['app_user', 'card']

admin.site.register(Card, CardAdmin)