from rest_framework import serializers
from .models import Room, Deck, Card
from registration.models import AppUser


class App_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['user', 'full_name', 'slug']

class Room_status_api_Serializer(serializers.ModelSerializer):
    person_1 = App_User_Serializer()
    person_2 = App_User_Serializer()
    person_3 = App_User_Serializer()
    person_4 = App_User_Serializer()
    class Meta:
        model = Room
        fields = ['person_1', 'person_2', 'person_3', 'person_4', 'room_code']


class Deck_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['suit', 'card_no', 'priority', 'point', 'img']

class Card_Serializer(serializers.ModelSerializer):
    card = Deck_Serializer()
    class Meta:
        model = Card
        fields = ['card']

