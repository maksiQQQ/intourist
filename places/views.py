from django.shortcuts import render, HttpResponse
from .models import Place


def places(request):
    places_objects = Place.objects.all() #Select * From Place

    return render(request, 'places.html', {'places': places_objects})
