from django.contrib import admin
from .models import Game, Sport, Event
from .models import Medal, Athlete, AthleteEvent
from .models import Team, Noc, Region

admin.site.register(Game)
admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Medal)
admin.site.register(Athlete)
admin.site.register(AthleteEvent)
admin.site.register(Team)
admin.site.register(Noc)
admin.site.register(Region)
