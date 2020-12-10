from rest_framework import serializers
from .models import Game, Sport, Event, Medal, Athlete, Region, Noc, Team, AthleteEvent


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = Event
        fields = ['id', 'name', 'sport']


class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Athlete
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class NocSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Noc
        fields = ['id', 'flag', 'region']


class TeamSerializer(serializers.ModelSerializer):
    noc = NocSerializer()

    class Meta:
        model = Team
        fields = ['id', 'name', 'noc']


class AthleteEventSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    event = EventSerializer()
    athlete = AthleteSerializer()
    team = TeamSerializer()

    class Meta:
        model = AthleteEvent
        fields = [
            'id',
            'game',
            'event',
            'athlete',
            'team',
            'athlete_height',
            'athlete_weight',
            'athlete_age'
        ]
