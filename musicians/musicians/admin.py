from django.contrib import admin

from .models import Musician, Song, Genre, UserFavoriteMusicians

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(UserFavoriteMusicians)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass

