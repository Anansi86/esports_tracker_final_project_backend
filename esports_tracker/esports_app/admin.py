from django.contrib import admin
from .models import Match, Team


class MatchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Match, MatchAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team, TeamAdmin)