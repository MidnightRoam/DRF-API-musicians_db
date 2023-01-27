from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Musician, Song
from .serializers import MusiciansSerializer, SongsSerializer
from .permissions import IsAuthorOrAdminOrReadOnly


# class MusicianAPIList(generics.ListCreateAPIView):
#     """List of all musician in database"""
#     serializer_class = MusiciansSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def get_queryset(self):
#         return Musician.objects.all()
#
#
# class MusicianAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     """Detail musician view"""
#     serializer_class = MusiciansSerializer
#     permission_classes = (IsAuthorOrAdminOrReadOnly, )
#
#     def get_queryset(self):
#         return Musician.objects.all()


class SongsViewSet(ModelViewSet):
    """List of all songs in database"""
    serializer_class = SongsSerializer
    queryset = Song.objects.prefetch_related('musician_set').all()
    filterset_fields = ('title', )
    search_fields = ('title', 'url')
    ordering_fields = ('title', )

# class SongsApiList(generics.ListCreateAPIView):
#     """List of all songs in database"""
#     serializer_class = SongsListSerializer
#
#     def get_queryset(self):
#         return Song.objects.prefetch_related('musician_set').all()


class MusicianViewSet(ModelViewSet):
    """Musician model viewset"""
    queryset = Musician.objects.all()
    serializer_class = MusiciansSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrAdminOrReadOnly)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('nickname', 'first_name', 'last_name')
    search_fields = ('nickname', 'first_name', 'last_name')
    ordering_fields = ('genre', 'age')

    # def list(self, request, *args, **kwargs):
    #     """List of all musician in database"""
    #     return Musician.objects.all()
    #
    # def retrieve(self, request, *args, **kwargs):
    #     """Detail musician"""
    #     return Musician.objects.all()


class SocialAuth(APIView):
    """Social auth API View"""
    def get(self, request):
        return render(request, 'oauth.html')


