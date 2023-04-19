from django.shortcuts import render
from django.http import HttpResponse

from .models import Game

def index(request):
    game = Game.objects.all()
    context = {
        'game': game, 
               }
    return render(request, 'main/index.html', context)