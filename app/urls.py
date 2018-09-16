from django.conf.urls import url

from . import views
from app.views import leaderboardViewSet

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^matches/$', views.matches , name='matches'),
    url(r'^match/(?P<id>[0-9]+)$', views.create_team , name='create_team'),
    url(r'^rules/$', views.rules , name='rules'),
    url(r'^leaderboard/$', views.leaderboard , name='leaderboard'),
    url(r'^listteams', views.listTeams , name='list_team'),
    url(r'^matchpoints', views.matchpoints , name='matchpoints'),
    url(r'^api/leaderboard$',leaderboardViewSet.as_view(), name='view-leaderboard'),
]
