from rest_framework import serializers
from .models import Match, Team, Player, Hero, Hero_player_matches, Match_score

class Match_scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match_score
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    scores = Match_scoreSerializer(many=True)
    class Meta:
        model = Match
        fields = "__all__"

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"

class Hero_player_matchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_player_matches
        fields = "__all__"

