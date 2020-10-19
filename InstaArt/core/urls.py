from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'styles', views.StyleViewSet)
router.register(r'pieces', views.PieceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
