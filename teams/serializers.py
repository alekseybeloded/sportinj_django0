from rest_framework import serializers
from .models import Team, Player, Injury


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class Injury_serializer(serializers.ModelSerializer):
    class Meta:
        model = Injury
        fields = '__all__'
