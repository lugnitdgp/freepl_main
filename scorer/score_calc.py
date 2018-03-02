from pycricbuzz import Cricbuzz
import json
import re
c=Cricbuzz()
def fetch_match():

	counter = 0
	matches = c.matches()
	for match in matches:
		#returns the position of the found string
		country_check = re.search('ENG',str(match))
		match_type = re.search('ODI',str(match))
		#print ("\n",match,"\n")
		print (country_check,match_type)
		if(match_type is None or country_check is None):
			counter+=1
			if ( counter==len(matches) ):
				print ("No Live match for England ")
		else:
			print (match)
			#Match found. Now calling create squad function
			create_squad(match)
			break

def create_squad(match):
	file = open ("scorecard.txt","w+")
	comment=c.commentary(match['id'])
	for i in range (2,4):
		#print (comment['commentary'][i])
		comm=comment['commentary'][i]
		print (comm)
	#print (json.dumps((comment),indent=4))
	#print ("\n",match,"\n")
fetch_match()