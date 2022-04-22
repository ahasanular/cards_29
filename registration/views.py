#for local use
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
from .models import AppUser

#for api use
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_208_ALREADY_REPORTED
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken


#function based page view

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_out(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('access_token')  # key must be added
    response.delete_cookie('refresh_token')  # key must be added
    response.delete_cookie('name')  # key must be added
    response.delete_cookie('slug')  # key must be added
    return response


#all api's

#sign_up_api
class Sign_up(CreateAPIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if 'name' not in data or data['name'] == '':
                feedback = {}
                feedback['message'] = "Name can't be null!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'email' not in data or data['email'] == '':
                feedback = {}
                feedback['message'] = "Email can't be null!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'password' not in data or data['password'] == '':
                feedback = {}
                feedback['message'] = "Password can't be null!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            user = User.objects.filter(email=data['email']).first()

            username = data['email'].split('@')

            if not user:
                user = User()
                user.username = username[0]
                user.email = data['email']
                user.first_name = data['name']
                user.password = make_password(data['password'])
                user.is_active = True

                app_user = AppUser()
                app_user.user = user
                app_user.email = data['email']
                app_user.full_name = data['name']

                user.save()
                app_user.save()

                feedback = {}
                feedback['message'] = "SuccessFully signed Up!"
                feedback['status'] = HTTP_200_OK
                return Response(feedback)
            else:
                feedback = {}
                feedback['message'] = "User Already Exist !"
                feedback['status'] = HTTP_208_ALREADY_REPORTED
                return Response(feedback)
        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_500_INTERNAL_SERVER_ERROR
            return Response(feedback)


#sign_in_api
class Sign_in(CreateAPIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                feedback = {}
                feedback['message'] = "Email can't be null!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'password' not in data or data['password'] == '':
                feedback = {}
                feedback['message'] = "Password can't be null!"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            user = User.objects.filter(Q(email=data['email']) | Q(username=data['email'])).first()


            if not user or user == '':
                feedback = {}
                feedback['message'] = "No Account Exist with this email or username"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            elif not user.is_active:
                feedback = {}
                feedback['message'] = "You need to activate your account first !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            else:
                if not check_password(data['password'], user.password):
                    feedback = {}
                    feedback['message'] = "Invalid Password!"
                    feedback['status'] = HTTP_401_UNAUTHORIZED
                    return Response(feedback)
                else:
                    app_user = AppUser.objects.filter(user=user).first()

                    token = RefreshToken.for_user(user)
                    feedback = {}
                    feedback['access_token'] = str(token.access_token)
                    feedback['refresh_token'] = str(token)
                    feedback['name'] = app_user.full_name
                    feedback['slug'] = app_user.slug
                    feedback['status'] = HTTP_200_OK
                    return Response(feedback)
        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_500_INTERNAL_SERVER_ERROR
            return Response(feedback)

