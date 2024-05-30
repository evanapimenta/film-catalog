"""
Serializers for movie APIs
"""

from rest_framework import serializers

from catalog.models import Movie, Show


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for movies."""
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genre', 'synopsis']
        read_only_fields = ['id']


class ShowSerializer(serializers.ModelSerializer):
    """Serializer for shows."""
    class Meta:
        model = Show
        fields = ['id', 'title', 'year', 'genre', 'synopsis']
        read_only_fields = ['id']