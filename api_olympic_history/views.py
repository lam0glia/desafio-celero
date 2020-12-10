from rest_framework import viewsets
from .models import Game, Sport, Event, Medal, Athlete, Region, Noc, Team, AthleteEvent
from .serializers import GameSerializer, SportSerializer, EventSerializer, MedalSerializer, AthleteSerializer, RegionSerializer, NocSerializer, TeamSerializer, AthleteEventSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class NocViewSet(viewsets.ModelViewSet):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AthleteEventViewSet(viewsets.ModelViewSet):
    queryset = AthleteEvent.objects.all()
    serializer_class = AthleteEventSerializer
