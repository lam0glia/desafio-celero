"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api_olympic_history.views import GameViewSet, SportViewSet, EventViewSet, MedalViewSet, AthleteViewSet, RegionViewSet, NocViewSet, TeamViewSet, AthleteEventViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'sports', SportViewSet)
router.register(r'events', EventViewSet)
router.register(r'medals', MedalViewSet)
router.register(r'athletes', AthleteViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'nocs', NocViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'athlete-events', AthleteEventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
