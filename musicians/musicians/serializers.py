from rest_framework import serializers

from .models import Musician, Song


class MusiciansListSerializer(serializers.ModelSerializer):
    """Musician list serializer"""
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Make a logged user as post author
    # when creating a post

    class Meta:
        model = Musician
        fields = '__all__'


class MusicianDetailSerializer(serializers.ModelSerializer):
    """Musician detail serializer"""
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Make a logged user as post author
    # when creating a post

    class Meta:
        model = Musician
        fields = '__all__'


class SongsListSerializer(serializers.ModelSerializer):
    """Songs list serializer"""
    class Meta:
        model = Song
        fields = '__all__'
