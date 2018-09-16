from django.contrib import admin

# Register your models here.
from import_export import resources
from app.models import Person, Player, PlayertoMatch, PersontoPM, Match
from import_export.admin import ImportExportModelAdmin

class PlayerResource(resources.ModelResource):

    class Meta:
        model = Player

class leaderboardmodeladmin(admin.ModelAdmin):
	list_display = ['_name','_email','_score']

class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource
    pass

#admin.site.register(Person,leaderboardmodeladmin)