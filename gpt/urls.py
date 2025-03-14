from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('chat_bot/', views.chat_bot, name='chat_bot'),
]
