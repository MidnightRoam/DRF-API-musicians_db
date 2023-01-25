from django.contrib import admin

from .models import Musician, Song, Genre

admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Genre)

