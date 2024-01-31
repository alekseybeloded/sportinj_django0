from rest_framework import viewsets
from .models import Team, Player, Injury
from .serializers import TeamSerializer, PlayerSerializer, Injury_serializer



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class InjuryViewSet(viewsets.ModelViewSet):
    queryset = Injury.objects.all()
    serializer_class = Injury_serializer
