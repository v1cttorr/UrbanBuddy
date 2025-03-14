from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.interests_ideas, name='interests_ideas'),
]
