from django.shortcuts import render


def home(request):
    return render(request, "hotel/index.html")


def rooms(request):
    return render(request, "hotel/rooms.html")


def about(request):
    return render(request, "hotel/about.html")


def contact(request):
    return render(request, "hotel/contact.html")
