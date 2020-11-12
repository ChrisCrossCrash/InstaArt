from InstaArt.core.models import Artist, Location, Style, Piece

from rest_framework import serializers


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['url', 'name', 'biography']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['url', 'name', 'city', 'country', 'web_site_url', 'description']


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Style
        fields = ['url', 'name', 'description']


class PieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Piece
        fields = ['url', 'title', 'artist', 'location', 'styles', 'description', 'created_date', 'wiki_url', 'image']


class InstaArtListSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer()
    location = LocationSerializer()
    styles = StyleSerializer(many=True)

    class Meta:
        model = Piece
        fields = [
            'title',
            'artist',
            'location',
            'styles',
            'description',
            'wiki_url',
            'image',
        ]
