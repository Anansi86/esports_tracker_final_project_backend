from django.db import models

class Matches(models.Model):
    win = models.CharField(max_length=25, blank=False, unique=True)
    video_url = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.IntegerField()
  #  team1 = models.ForeignKey(Teams,on_delete=models.SET_NULL, null=True)
  #  team2 = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True)
  #  status = models.IntegerField()