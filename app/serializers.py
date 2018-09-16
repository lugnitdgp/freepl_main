from app.models import *
import collections
from rest_framework import serializers

class leaderboardserializer(serializers.ModelSerializer):

	class Meta:

		model = Person
		fields = ('name', 'email', 'total_score') 