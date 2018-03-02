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
	file = open ("playerlist.txt","w")
	comment=c.commentary(match['id'])
	for i in range (2,4):
		#get the squad list of both the teams in the dic keyword commentray
		comm=comment['commentary'][i]
		new_comm = re.split(',|:',str(comm))
		print (len(new_comm))
		for player in new_comm:
			file.write(str(player)+"\n")
	file.close()
	#Write the data in a CSV file for easier import.


fetch_match()