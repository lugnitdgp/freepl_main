from pycricbuzz import Cricbuzz
import json
def calculate_score():
	#for batsman
	players=[]
	sixes=0
	fours=0
	runs=0
	balls_faced=0
	c=Cricbuzz()
	file = open ('playerlist.txt','r')
	for line in file:
		players.append(line.strip())
	print (players)

	matches=c.matches()
	score_card=c.scorecard(match['id'])


calculate_score()
