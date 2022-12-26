from django.db import models

# Create your models here.


class Hockeyteam(models.Model):
    matchNumber = models.IntegerField()
    roundNumber = models.IntegerField()
    dateUtc = models.DateField()
    location = models.CharField(max_length=100)
    homeTeam = models.CharField(max_length=100)
    awayTeam = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)
    homeTeamScore = models.IntegerField(null=True)
    awayTeamScore = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.location}"