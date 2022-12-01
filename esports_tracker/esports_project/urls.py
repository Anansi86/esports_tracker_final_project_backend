from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from esports_app import views
from esports_app.views import MatchViewSet, TeamViewSet, PlayerViewSet, HeroViewSet, Hero_player_matchesViewSet, Match_scoreViewSet

router = routers.DefaultRouter()
router.register(r'match', views.MatchViewSet)
router.register(r'team', views.MatchViewSet)
router.register(r'player', views.PlayerViewSet)
router.register(r'hero', views.HeroViewSet)
router.register(r'hero_player_matches', Hero_player_matchesViewSet)
router.register(r'match_score', views.Match_scoreViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
