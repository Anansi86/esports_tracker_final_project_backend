from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)
    icon = models.URLField()

class Match(models.Model):
    win = models.CharField(max_length=25, blank=False, unique=True)
    video_url = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.IntegerField()
    team1 = models.ForeignKey(Team,on_delete=models.SET_NULL, null=True, related_name="Team1" )
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="Team2")
    status = models.IntegerField()

class Player(models.Model):
    player_name = models.CharField(max_length=25, blank=False, unique=True)
    alias_name = models.CharField(max_length=25, blank=False, unique=True)
    player_num = models.IntegerField()
    hometown = models.CharField(max_length=25, blank=False, unique=True)
    pic = models.URLField()
