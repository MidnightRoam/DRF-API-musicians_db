from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Musician, Song, UserFavoriteMusicians
from .serializers import MusiciansSerializer, SongsSerializer, UserMusicianRelationSerializer
from .permissions import IsAuthorOrStaffOrReadOnly, IsStaffOrReadyOnly


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
    permission_classes = (IsStaffOrReadyOnly, )
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
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrStaffOrReadOnly)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('nickname', 'first_name', 'last_name')
    search_fields = ('nickname', 'first_name', 'last_name')
    ordering_fields = ('genre', 'age')

    def perform_create(self, serializer):
        """Automatically choosing current user as post author while creating"""
        serializer.validated_data['post_author'] = self.request.user
        serializer.save()

    # def list(self, request, *args, **kwargs):
    #     """List of all musician in database"""
    #     return Musician.objects.all()
    #
    # def retrieve(self, request, *args, **kwargs):
    #     """Detail musician"""
    #     return Musician.objects.all()


class UserMusicianRelationsView(UpdateModelMixin, GenericViewSet):
    """
    Relation between user and musician models that include a
    functionality of rate musician, add to favorite by user
    """
    permission_classes = (IsAuthenticated, )
    queryset = UserFavoriteMusicians.objects.all()
    serializer_class = UserMusicianRelationSerializer
    lookup_field = 'musician'

    def get_object(self):
        obj, created = UserFavoriteMusicians.objects.get_or_create(user=self.request.user,
                                                                   musician_id=self.kwargs['musician'])
        return obj


class SocialAuth(APIView):
    """Social auth API View"""
    def get(self, request):
        return render(request, 'oauth.html')
