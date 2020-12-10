from rest_framework import serializers
from .models import Game, Sport, Event, Medal, Athlete, AthleteEvent


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Athlete
        fields = '__all__'


class AthleteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteEvent
        fields = '__all__'
