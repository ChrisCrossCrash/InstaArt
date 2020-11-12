from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('artists', views.ArtistViewSet)
router.register('locations', views.LocationViewSet)
router.register('styles', views.StyleViewSet)
router.register('pieces', views.PieceViewSet)
router.register('insta', views.InstaArtListViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
