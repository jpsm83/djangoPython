from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # dinamic route for rooms
    path('room/<str:pk>', views.room, name='room'),
]
