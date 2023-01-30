from rest_framework import serializers

from .models import Musician, Song, UserFavoriteMusicians


class MusiciansSerializer(serializers.ModelSerializer):
    """Musician model serializer"""
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Make a logged user as post author
    # when creating a post

    class Meta:
        model = Musician
        fields = '__all__'


class SongsSerializer(serializers.ModelSerializer):
    """Songs list serializer"""
    class Meta:
        model = Song
        fields = '__all__'


class UserMusicianRelationSerializer(serializers.ModelSerializer):
    """User - musician relation serializer"""
    class Meta:
        model = UserFavoriteMusicians
        fields = ('musician', 'like', 'in_favorite', 'rate')
