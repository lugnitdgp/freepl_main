import csv
from app.models import Person, Player, PlayertoMatch, PersontoPM, Match
import os
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freepl_main.settings')
# to run this file, do python3 manage.py shell and then do exec(open("load.py").read())

perform = PersontoPM.objects.all()
for i in perform:
    ptm=i.pm
    sco=ptm.score
    if i.power_player==True:
        sco=2*sco
    i.score=sco
    i.save()

    
    
