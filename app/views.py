from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Person, Player, PlayertoMatch, PersontoPM, Match

# Create your views here.
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user
        try:
            person = Person.objects.get(user=profile)
        except:
            person = Person(user=profile)
            person.email = user.email
            person.name = response.get('name')
            person.save()

    elif backend.name == 'google-oauth2':
        profile = user
        try:
            person = Person.objects.get(user=profile)
        except:
            person = Person(user=profile)
            person.email = user.email
            person.name = response.get('name')['givenName'] + " " + response.get('name')['familyName']
            person.save()

def index(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/matches')
    return render(request, 'index_page.html', {})

@login_required
def matches(request):
    matches = Match.objects.all()
    return render(request,'matches.html',{'matches':matches})

@login_required
def create_team(request,id):
    match = get_object_or_404(Match, pk=id)
    all_players = Player.objects.filter(country = match.country1) + Player.objects.filter(country = match.country2)
    print (match.country1)
    if request.method == 'GET':
        return render(request,'create_team.html',{'players': all_players })
    else:
        return
    return

def leaderboard(request):
    persons = Person.objects.all()
    persons.sort(key = lambda x : x.score, reverse=True)
    return render(request,'leaderboard.html',{'persons': persons})