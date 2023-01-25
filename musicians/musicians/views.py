from rest_framework import generics
from rest_framework.response import Response

from .models import Musician
from .serializers import MusiciansListSerializer, MusicianDetailSerializer


class MusicianAPIList(generics.ListCreateAPIView):
    """List of all musician in database"""
    serializer_class = MusiciansListSerializer

    def get_queryset(self):
        return Musician.objects.all()


class MusicianAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail musician view"""
    serializer_class = MusicianDetailSerializer

    def get_queryset(self):
        return Musician.objects.all()
