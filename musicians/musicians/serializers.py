from rest_framework import serializers

from .models import Musician, Song, UserFavoriteMusicians, UserSongRelation


class MusiciansSerializer(serializers.ModelSerializer):
    """Musician model serializer"""
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Make a logged user as post author
    # while creating a post
    likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    in_favorites = serializers.IntegerField()

    class Meta:
        model = Musician
        fields = ('first_name', 'last_name', 'nickname', 'content', 'age', 'city',
                  'country', 'image', 'genre', 'songs', 'post_author', 'likes_count', 'annotated_likes',
                  'rating', 'in_favorites')

    def get_likes_count(self, instance):
        """Get musician likes count"""
        return UserFavoriteMusicians.objects.filter(musician=instance, like=True).count()


class SongsSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    in_favorites = serializers.IntegerField()

    """Songs list serializer"""
    class Meta:
        model = Song
        fields = ('title', 'url', 'likes_count', 'annotated_likes', 'rating', 'in_favorites')

    def get_likes_count(self, instance):
        """Get songs likes count"""
        return UserSongRelation.objects.filter(song=instance, like=True).count()


class UserMusicianRelationSerializer(serializers.ModelSerializer):
    """User - musician relation serializer"""
    class Meta:
        model = UserFavoriteMusicians
        fields = ('musician', 'like', 'in_favorite', 'rate')
