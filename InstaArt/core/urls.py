from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api/', views.InstaArt.as_view()),
    path('api/artist/<int:pk>/', views.ArtistView.as_view()),
    path('api/location/<int:pk>/', views.LocationView.as_view()),
    path('api/style/<int:pk>/', views.StyleView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
