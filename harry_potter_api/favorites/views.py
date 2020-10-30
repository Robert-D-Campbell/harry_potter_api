from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Favorite
from .forms import *
from decouple import config
import requests

# Create your views here.
def characters(request):
    key = config("HARRY_POTTER_API_KEY")
    url = "https://www.potterapi.com/v1/characters/?key={}"

    characters = requests.get(url.format(key)).json()
    # print(characters)
    # character_data = {}

    for character in characters:

        character_data = {
            "name": character["name"],
            "house": 'n/a',
            "blood_status": character["bloodStatus"],
            "species": character["species"],
        }
        print(character_data)
        form = FavoriteForm(initial=character_data)
    
    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"characters": characters, "form": form}
    return render(request, "characters/characters_list.html", context)


def favorites_list(request):
    favorites = Favorite.objects.all()

    context = {"favorites": favorites}
    return render(request, "favorites/favorites_list.html", context)


def favorite_detail(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)

    context = {"favorite": favorite}
    return render(request, "favorites/favorite_detail.html", context)
