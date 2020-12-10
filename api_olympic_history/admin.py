from django.contrib import admin
from .models import Game, Sport, Event, Medal, Athlete, AthleteEvent


admin.site.register(Game)
admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Medal)
admin.site.register(Athlete)
admin.site.register(AthleteEvent)
