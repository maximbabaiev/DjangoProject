from django.shortcuts import render
from Lesson_13_Model_JSON.models import Hockeyteam
import datetime
from django.http import HttpResponse
import json
# Create your views here.


def upload_data(request):
    with open('products.json', "r") as f:
        reader = json.load(f)
        for row in reader:
            print(row)
            try:
                date = row.get("DateUtc")[0:10].split("-")
                time = row.get("DateUtc")[11:19].split(":")
                _, created = Hockeyteam.objects.get_or_create(
                    matchNumber=row.get("MatchNumber"),
                    roundNumber=row.get("RoundNumber"),
                    dateUtc=datetime.datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]),
                                              hour=int(time[0]), minute=int(time[1]), second=int(time[2])),
                    location=row.get("Location"),
                    homeTeam=row.get("HomeTeam"),
                    awayTeam=row.get("AwayTeam"),
                    group=row.get("Group"),
                    homeTeamScore=row.get("HomeTeamScore"),
                    awayTeamScore=row.get("AwayTeamScore"),

                )
            except Exception as ex:
                print(ex)
                pass
    return HttpResponse("Done!")
