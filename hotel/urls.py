from django.urls import path

from . import views

app_name = "hotel"

urlpatterns = [
    path("", views.home, name="home"),
    path("rooms/", views.rooms, name="rooms"),
    path("contact/", views.contact, name="contact"),
]
