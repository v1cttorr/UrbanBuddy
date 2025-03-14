from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('chat_bot/ask/', views.ask_chat_bot, name='ask_chat_bot'),
]
