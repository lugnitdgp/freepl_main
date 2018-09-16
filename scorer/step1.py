import csv
from app.models import Player
import os
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freepl_main.settings')
# to run this file, do python3 manage.py shell and then do exec(open("step1.py").read())

#for i in Player.objects.all():
#    i.delete()

with open('players.csv') as f:
    reader=csv.DictReader(f)
    for row in reader:
        p=(row['Player Name'].strip())
        c="".join(row['Cost'].split())

        r="".join(row['Role'].split())
        n="".join(row['Country'].split())
        c=int(c)
        z=Player(name=p,cost=c,role=r,country=n)
        z.save()
        

