from app.models import *
import collections
from rest_framework import serializers

class leaderboardserializer(serializers.ModelSerializer):

	class Meta:

		model = Person
		fields = ('user_name','name', 'email', 'total_score') 