from django.db import models


class Game(models.Model):
    season = models.CharField(max_length=6)
    year = models.IntegerField()

    def __str__(self):
        return '%s %d' % (self.season, self.year)


class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Medal(models.Model):
    type = models.CharField(max_length=6, null=True)

    def __str__(self):
        return "%s" % (self.type)


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)

    def __srt__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=100, null=True, blank=True)

    def __self(self):
        return self.name


class Noc(models.Model):
    flag = models.CharField(max_length=3)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )

    def __str__(self):
        return self.flag


class Team(models.Model):
    name = models.CharField(max_length=100)
    noc = models.ForeignKey(Noc, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AthleteEvent(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    medal = models.ForeignKey(Medal, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    athlete_height = models.CharField(max_length=3, null=True)
    athlete_weight = models.CharField(max_length=5, null=True)
    athlete_age = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.athlete_age
