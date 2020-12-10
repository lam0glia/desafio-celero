from rest_framework import viewsets
from .models import Game, Sport, Event, Medal, Athlete, AthleteEvent
from .serializers import GameSerializer, SportSerializer, EventSerializer, MedalSerializer, AthleteSerializer, AthleteEventSerializer


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


class AthleteEventViewSet(viewsets.ModelViewSet):
    queryset = AthleteEvent.objects.all()
    serializer_class = AthleteEventSerializer
