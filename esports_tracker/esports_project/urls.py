from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from esports_app import views
from esports_app.views import MatchViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'Match', views.MatchViewSet)
router.register(r'Team', views.MatchViewSet)

Match_list = MatchViewSet.as_view({
    'get': 'list'
})

Team_list = TeamViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('match', Match_list, name='Match-list'),
    path('team', Team_list, name= 'Team-list'),
]
