from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game, Sport, Event, Medal, Athlete, Region, Noc, Team, AthleteEvent
from .serializers import GameSerializer, SportSerializer, EventSerializer, MedalSerializer, AthleteSerializer, RegionSerializer, NocSerializer, TeamSerializer, AthleteEventSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season', 'year']

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class NocViewSet(viewsets.ModelViewSet):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['flag']


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class AthleteEventViewSet(viewsets.ModelViewSet):
    queryset = AthleteEvent.objects.all()
    serializer_class = AthleteEventSerializer
