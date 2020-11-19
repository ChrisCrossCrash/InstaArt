from django.contrib import admin

from .models import Artist, Location, Style, Piece

admin.site.register(Artist)
admin.site.register(Location)
admin.site.register(Style)
admin.site.register(Piece)
