from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.event, name='event'),
]
