from rest_framework import routers
from .views import TeamViewSet, PlayerViewSet, InjuryViewSet


team_router = routers.SimpleRouter()
team_router.register(r'teams', TeamViewSet)

player_router = routers.SimpleRouter()
player_router.register(r'players', PlayerViewSet)

injury_router = routers.SimpleRouter()
injury_router.register(r'injuries', InjuryViewSet)
