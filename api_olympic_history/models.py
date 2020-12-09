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
    type = models.CharField(max_length=6)

    def __str__(self):
        return self.type
