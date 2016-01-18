from django.contrib.auth.models import User
from django.db import models
import datetime

from django.contrib import admin

class Person(models.Model):
    class Meta:
        db_table = 'person'

    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default="")
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Match(models.Model):
    class Meta:
        db_table = 'match'

    country1 = models.TextField(max_length=100, default="")
    country2 = models.TextField(max_length=100, default="")
    day = models.DateField(default=datetime.datetime.today())

    def __str__(self):
        return self.country1

class Player(models.Model):
    class Meta:
        db_table = 'player'

    name = models.TextField(max_length=10, default="")
    country = models.TextField(max_length=10, default="")
    cost = models.IntegerField(default=0)
    role = models.TextField(max_length=25,default="")

class PlayertoMatch(models.Model):
    class Meta:
        db_table = 'PlayertoMatch'

    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.player.name + "for the match " + self.match.country1 + 'vs' + self.match.country2 + "scored : " + str(self.score)