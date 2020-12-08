from django.db import models


class Game(models.Model):
    season = models.CharField(max_length=6)
    year = models.IntegerField()

    def __str__(self):
        return '%s %d' % (self.season, self.year)
