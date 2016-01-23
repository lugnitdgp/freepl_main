from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^matches/$', views.matches , name='matches'),
    url(r'^match/(?P<id>[0-9]+)$', views.create_team , name='create_team'),
    # url(r'^rules/$', views.rules , name='rules'),
    # url(r'^ranking/$', views.ranking , name='ranking'),
]
