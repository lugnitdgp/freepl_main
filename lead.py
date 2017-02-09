import csv
from app.models import Person, Player, PlayertoMatch, PersontoPM, Match
from django.db.models import Sum
import os
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freepl_main.settings')
# to run this file, do python3 manage.py shell and then do exec(open("load.py").read())

person = Person.objects.all()
for i in person:
    f=PersontoPM.objects.filter(person=i)
    if len(f)>0 :
        t=PersontoPM.objects.filter(person=i).aggregate(sum=Sum('score'))['sum']
        i.total_score=t
        i.save()    
    
 
