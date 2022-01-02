from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:pk>", views.room, name="room"),
    
    path("create-room/", views.createRoom, name="create-room")
]