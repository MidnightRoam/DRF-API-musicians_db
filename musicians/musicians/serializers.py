from rest_framework import serializers

from .models import Musician


class MusiciansListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class MusicianDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'
