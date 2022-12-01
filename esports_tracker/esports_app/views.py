from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Match, Team, Player, Hero, Hero_player_matches, Match_score
from .serializers import MatchSerializer, TeamSerializer, PlayerSerializer, HeroSerializer, Hero_player_matchesSerializer, Match_scoreSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all().order_by("created")

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all().order_by("name")

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all().order_by("player_name")

class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all().order_by("name")

class Hero_player_matchesViewSet(viewsets.ModelViewSet):
    serializer_class = Hero_player_matchesSerializer
    queryset = Hero_player_matches.objects.all().order_by("points")

class Match_scoreViewSet(viewsets.ModelViewSet):
    serializer_class = Match_scoreSerializer
    queryset = Match_score.objects.all().order_by("match_id")
