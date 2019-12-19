
from django.contrib import admin
from django.urls import path
from quotes_app.views import quotes_list, quote_featured

urlpatterns = [
    path('all/', quotes_list),
    path('featured/', quote_featured)
    
]
