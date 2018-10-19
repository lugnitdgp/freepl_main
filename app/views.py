from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Person, Player, PlayertoMatch, PersontoPM, Match
from app.serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class leaderboardViewSet(ListAPIView):
    queryset = Person.objects.all().order_by('-total_score')
    serializer_class = leaderboardserializer

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user
        try:
            person = Person.objects.get(user=profile)
        except:
            person = Person(user=profile)
            person.email = user.email
            person.user_name = user.username
            person.name = response.get('name')
            person.save()

    elif backend.name == 'google-oauth2':
        profile = user
        try:
            person = Person.objects.get(user=profile)
        except:
            person = Person(user=profile)
            person.email = user.email
            person.user_name = user.username
            person.name = response.get('name')['givenName'] + " " + response.get('name')['familyName']
            person.save()

def index(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/matches')
    return render(request, 'index.html', {})

@login_required
def matches(request):
    all_matches = Match.objects.all()
    return render(request,'matches.html',{'matches':all_matches})

"""TODO : Create a new python script to populate the database
 for players as well as matches, also player to match so that we dont have to do it here """

@login_required
def create_team(request,id):
    match = get_object_or_404(Match, pk=id)
    if match.can_edit == False:
            messages.error(request, "Match is locked. Cannot change players")
            return HttpResponseRedirect('/matches')
    all_players = []
    for i in Player.objects.filter(country = match.country1):
        all_players.append(i)
    for i in Player.objects.filter(country = match.country2):
        all_players.append(i)
    #print (match.country1)
    person = Person.objects.get(user_id = request.user.pk)
    if request.method == 'GET':
        if len(PersontoPM.objects.filter(person=person, pm__match=match))!=0:
            messages.success(request,"You have already selected a team. If you select again, the previous team will be overwritten")
        return render(request,'create_team.html',{'players': all_players, 'id':id})
    else:
        players = request.POST.getlist('sport')
        if len(players)!=11:
            messages.error(request, "You should choose exactly 11 players")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        captain = request.POST['captain']
        if captain not in players:
            messages.error(request, "Don't try stupid stuff")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        player_class = []
        bats=0
        bowl=0
        wk=0
        allr=0
        c1=0
        c2=0
        money = 0
        for i in players:
            p=Player.objects.get(name=i)
            player_class.append(p)
            print (player_class)
            money+=p.cost
            print (money)
            if p.role == 'Batsman': bats+=1
            elif p.role == 'AllRounder': allr+=1
            elif p.role == 'WicketKeeper': wk+=1
            elif p.role =='Bowler': bowl+=1
            if p.country == match.country1: c1+=1
            else: c2+=1
        if bats<4:
            messages.error(request, "You should choose a minimum of 4 batsmen")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        elif allr<2:
            messages.error(request, "You should choose a minimum of 2 all rounders")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        elif wk!=1:
            messages.error(request, "You should choose exactly 1 wicket keeper")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        elif bowl<2:
            messages.error(request, "You should choose a minimum of 2 bowlers")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        elif c1>6 or c2>6:
            messages.error(request, "You can choose only a maximum of 6 players from one country")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        elif money>1000:
            messages.error(request,"Dude. Don't flatter yourself. You aren't that smart.")
            return render(request,'create_team.html',{'players': all_players, 'id':id })
        #remove all existing entries
        person2p2m = PersontoPM.objects.filter(person=person, pm__match = match)
        for i in person2p2m:
            i.delete()
        for i in player_class:
            print (i)
            m=PlayertoMatch.objects.get(match=match, player=i)            
            if i.name == captain:
                val=True
            else:
                val=False
            p=PersontoPM(person=person, pm = m, power_player = val)
            p.save()
        messages.success(request,"Your team has been selected")
        return HttpResponseRedirect('/matches')
    return

def leaderboard(request):
    persons = list(Person.objects.all())
    persons.sort(key = lambda x : x.total_score, reverse=True)
    return render(request,'leaderboard.html',{'persons': persons})




def rules(request):
    return render(request,'rules.html',{})

@login_required
def listTeams(request):
    matches = Match.objects.all()
    if request.method == 'GET':
        return render(request,'listteams.html',{'matches': matches})
    elif request.method == 'POST':
        id = request.POST['id']
        match=Match.objects.get(id=id)
        #print (match.country1)
        person = Person.objects.get(user_id = request.user.pk)
        players = PersontoPM.objects.filter(person=person, pm__match = match)
        p=[]
        for i in players:
            it={}
            it['play']=i.pm.player
            it['bool']=i.power_player
            p.append(it)

        p=list(p)
        return render(request,"listteams.html",{'players':p, 'matches': matches})

@login_required
def matchpoints(request):
    matches = Match.objects.all()
    if request.method == 'GET':
        return render(request,'listteams.html',{'matches': matches})
    elif request.method == 'POST':
        id = request.POST['id']
        mat=Match.objects.get(id=id)
        
        
        players = PlayertoMatch.objects.filter(match=mat)
        
        
        return render(request,"match_points.html",{'players':players, 'matches': matches})