
from django.contrib import admin
from django.urls import path
from friend_app.views import friends_name,best


urlpatterns = [
    path('all/', friends_name ),
    path('best/', best)
   
]
