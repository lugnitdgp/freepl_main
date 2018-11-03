from app.models import *
import collections
from rest_framework import serializers

class leaderboardserializer(serializers.ModelSerializer):

	score = serializers.IntegerField(source = '_score')
	class Meta:

		model = Person
		fields = ('user_name','name', 'email', 'score') 
