from django.contrib import admin
from .models import Match, Team, Player, Hero, Hero_player_matches, Match_score


class MatchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Match, MatchAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)

class HeroAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hero, HeroAdmin)

class Hero_player_matchesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hero_player_matches,  Hero_player_matchesAdmin)

class Match_scoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Match_score, Match_scoreAdmin)