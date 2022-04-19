from django.urls import path
from . import views

urlpatterns = [
    #function based views
    path('sign_up/', views.sign_up),
    path('sign_in/', views.sign_in),
    path('sign_out/', views.sign_out),

    #Class based api's
    path('sign_up_api/', views.Sign_up.as_view()),
    path('sign_in_api/', views.Sign_in.as_view()),
]