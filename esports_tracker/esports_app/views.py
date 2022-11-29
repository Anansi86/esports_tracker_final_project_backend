from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Match, Team
from .serializers import MatchSerializer, TeamSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all().order_by("created")

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all().order_by("name")