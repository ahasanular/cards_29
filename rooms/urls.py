from django.urls import path
from . import views

urlpatterns = [
    #function based view
    path('room/<str:id>/', views.room),

    #class based api's
    path('create_room_api/', views.Create_room_api.as_view()),
    path('room_status_api/<str:id>/', views.Room_status_api.as_view()),
    path('join_room_api/', views.Join_room_api.as_view()),
    path('join_seat_api/', views.Join_seat_api.as_view()),
    path('<str:id>/start_game_api/', views.Start_game_api.as_view()),
]