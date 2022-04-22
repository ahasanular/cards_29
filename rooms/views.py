import json

from django.shortcuts import render
from .models import Room
from registration.models import AppUser
import secrets

#for api's
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_208_ALREADY_REPORTED
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

#import full serializers
from . import serializers


#function based template view

def room(request, id):
    data = "abcd"
    return render(request, 'room.html')

class Create_room_api(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            if not request.user or request.user == '':
                feedback = {}
                feedback['message'] = "No user found for room !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)


            app_user = AppUser.objects.filter(user=request.user).first()

            room = Room.objects.filter(Q(person_1=app_user) | Q(person_2=app_user) | Q(person_3=app_user) | Q(person_4=app_user)).first()

            if not room:
                room = Room()
                room_code = str(secrets.token_hex(3))
                room.person_1 = app_user
                room.room_code = room_code
                room.save()

                feedback = {}
                feedback['message'] = "Room created successfully!"
                feedback['status'] = HTTP_200_OK
                feedback['room_code'] = room_code
                feedback['room_id'] = str(room.id)
                return Response(feedback)
            else:
                feedback = {}
                feedback['message'] = "You are already In a room!"
                feedback['status'] = HTTP_208_ALREADY_REPORTED
                feedback['room_code'] = room.room_code
                return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)

class Room_status_api(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            room = Room.objects.filter(id=id).first()

            print("before")
            print(room.person_1)
            print(room.person_2)

            if room.person_1 and room.person_1.user == request.user:
                pass
            elif room.person_2 and room.person_2.user == request.user:
                temp = room.person_1
                room.person_1 = room.person_2
                room.person_2 = room.person_3
                room.person_3 = room.person_4
                room.person_4 = temp

            elif room.person_3 and room.person_3.user == request.user:
                temp = room.person_1
                room.person_1 = room.person_3
                room.person_3 = temp

                temp = room.person_4
                room.person_4 = room.person_2
                room.person_2 = temp

            elif room.person_4 and room.person_4.user == request.user:
                temp = room.person_1
                room.person_1 = room.person_4
                room.person_4 = room.person_3
                room.person_3 = room.person_2
                room.person_2 = temp

                # room.person_1, room.person_2 = room.person_2, room.person_1
                # room.person_2, room.person_3 = room.person_3, room.person_2
                # room.person_3, room.person_4 = room.person_4, room.person_3

            print("after")
            print(room.person_1)
            print(room.person_2)


            if not room:
                feedback = {}
                feedback['message'] = "room not found with this ID !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            else:
                room = serializers.Room_status_api_Serializer(room).data
                room['status'] = HTTP_200_OK
                return Response(room)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)


class Join_room_api(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if not request.user or request.user == '':
                feedback = {}
                feedback['message'] = "No user found for room !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'join_code' not in data or data['join_code'] == '':
                feedback = {}
                feedback['message'] = "Please provide a valid join code"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            room = Room.objects.filter(room_code=data['join_code']).first()

            feedback = {}
            feedback['message'] = "Joined the room successfully!"
            feedback['status'] = HTTP_200_OK
            feedback['room_id'] = str(room.id)
            return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)

class Join_seat_api(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            if not request.user or request.user == '':
                feedback = {}
                feedback['message'] = "No user found for room !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'room_id' not in data or data['room_id'] == '':
                feedback = {}
                feedback['message'] = "Room Id can't be null !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            app_user = AppUser.objects.filter(user=request.user).first()

            room = Room.objects.filter(id=data['room_id']).first()

            if not room:
                feedback = {}
                feedback['message'] = "No Room found with this code!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            else:
                if 'seat_no' not in data or data['seat_no'] == '':
                    feedback = {}
                    feedback['message'] = "Please provide a valid Seat No !"
                    feedback['status'] = HTTP_400_BAD_REQUEST
                    return Response(feedback)

                if room.person_1 == app_user or room.person_2 == app_user or room.person_3 == app_user or room.person_4 == app_user:
                    feedback = {}
                    feedback['message'] = "You are already in a room!"
                    feedback['status'] = HTTP_400_BAD_REQUEST
                    return Response(feedback)

                if data['seat_no'] == "person_2":
                    room.person_2 = app_user
                elif data['seat_no'] == "person_3":
                    room.person_3 = app_user
                elif data['seat_no'] == "person_4":
                    room.person_4 = app_user

                room.save()
                feedback = {}
                feedback['message'] = "Joined seat successfully!"
                feedback['status'] = HTTP_200_OK
                feedback['room_id'] = str(room.id)
                return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)