from django.contrib import admin

from .models import Musician, Song, Genre

admin.site.register(Song)
admin.site.register(Genre)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass

