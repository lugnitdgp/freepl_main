import datetime
import csv
from app.models import Player,Match,PlayertoMatch,Person
import os
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freepl_main.settings')

# this file is used to add matches and playerto match entries., to run this file, follow the same instruction as in load.py

c1=input("Enter Country 1\n")
c2=input("Entry Country 2\n")
date_entry=input("Enter Date in YYYY-MM-DD format \n")
year,month,day=map(int,date_entry.split('-'))
date1=datetime.date(year,month,day)

print(c1,c2,date1)
m=Match(country1=c1,country2=c2,day=date1,can_edit=True)
m.save()

for i in Player.objects.all():
	for j in Match.objects.all():
		if j.day==date1:
	   		if i.country==c1 or i.country==c2:
	   			p=PlayertoMatch(match=m,player=i)
	   			p.save()