from django.urls import path

from InstaArt.core.views import say_hi


urlpatterns = [
    path('', say_hi)
]