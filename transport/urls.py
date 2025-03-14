from django.urls import path
from . import views

urlpatterns = [
    path('', views.transports, name='transports'),
    path('drive/<int:pk>/', views.transport, name='transport'),
    path('map/', views.map, name='map'),
]
