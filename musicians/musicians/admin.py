from django.contrib import admin

from .models import Musician, Song, Genre, UserFavoriteMusicians, UserSongRelation


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(UserFavoriteMusicians)
class UserFavoriteMusiciansAdmin(admin.ModelAdmin):
    pass


@admin.register(UserSongRelation)
class UserSongRelationAdmin(admin.ModelAdmin):
    pass
