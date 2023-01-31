from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Musician, Song, UserFavoriteMusicians, UserSongRelation


class MusicianListenerSerializer(serializers.ModelSerializer):
    """Musician listener serializer"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class MusiciansSerializer(serializers.ModelSerializer):
    """Musician model serializer"""
    # Make a logged user as post author while creating a post
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Musician user likes field
    annotated_likes = serializers.IntegerField(read_only=True)
    # Calculating the average rating of a musician field
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    # Track if the user has added a musician to their favorites field
    in_favorites = serializers.IntegerField()
    # Post author name field
    post_author_name = serializers.CharField(source='post_author.username', default="",
                                             read_only=True)
    # Musician listeners field
    listeners = MusicianListenerSerializer(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = ('first_name', 'last_name', 'nickname', 'content', 'age', 'city',
                  'country', 'image', 'genre', 'songs', 'post_author', 'annotated_likes',
                  'rating', 'in_favorites', 'post_author_name', 'listeners')


class SongsSerializer(serializers.ModelSerializer):
    # Song user likes field
    annotated_likes = serializers.IntegerField(read_only=True)
    # Calculating the average rating of a song
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    # Track if the user has added a musician to their favorites field
    in_favorites = serializers.IntegerField()

    """Songs list serializer"""
    class Meta:
        model = Song
        fields = ('title', 'url', 'annotated_likes', 'rating', 'in_favorites')


class UserMusicianRelationSerializer(serializers.ModelSerializer):
    """User - musician relation serializer"""
    class Meta:
        model = UserFavoriteMusicians
        fields = ('musician', 'like', 'in_favorite', 'rate')
