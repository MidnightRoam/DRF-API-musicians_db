from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg
from rest_framework.test import APITestCase

from musicians.serializers import SongsSerializer, MusiciansSerializer
from musicians.models import Song, Musician, UserFavoriteMusicians, UserSongRelation


# class SongsSerializerTest(APITestCase):
#     """Songs serializer tests"""
#
#     def test_ok(self):
#         user1 = User.objects.create(username='test_user1', is_staff=True)
#         user2 = User.objects.create(username='test_user2')
#         user3 = User.objects.create(username='test_user3')
#
#         song_1 = Song.objects.create(title="Test song 1", url='1')
#         song_2 = Song.objects.create(title="Test song 2", url='2')
#         song_3 = Song.objects.create(title="Test song 3", url='3')
#
#         UserSongRelation.objects.create(user=user1, song=song_1, like=True)
#         UserSongRelation.objects.create(user=user2, song=song_1, like=True)
#         UserSongRelation.objects.create(user=user3, song=song_1, like=True)
#
#         UserSongRelation.objects.create(user=user1, song=song_2, like=True)
#         UserSongRelation.objects.create(user=user2, song=song_2, like=True)
#         UserSongRelation.objects.create(user=user3, song=song_2, like=False)
#
#         songs = Song.objects.all().annotate(
#             annotated_likes=Count(Case(When(usersongrelation__like=True, then=1))))
#
#         data = SongsSerializer(songs, many=True).data
#
#         expected_data = [
#             {
#                 'id': song_1.id,
#                 'title': 'Test song 1',
#                 'url': '1'
#             },
#             {
#                 'id': song_2.id,
#                 'title': 'Test song 2',
#                 'url': '2'
#             },
#             {
#                 'id': song_3.id,
#                 'title': 'Test song 3',
#                 'url': '3'
#             },
#         ]
#         self.assertEqual(expected_data, data, 'Invalid data')


class MusiciansSerializerTest(APITestCase):
    """Musicians serializer test"""

    def test_ok(self):
        user1 = User.objects.create(username='test_user1', is_staff=True)
        user2 = User.objects.create(username='test_user2')
        user3 = User.objects.create(username='test_user3')

        musician_1 = Musician.objects.create(first_name="Aboba 1",
                                             age=18,
                                             post_author=user1)
        musician_2 = Musician.objects.create(first_name="Aboba 2",
                                             age=20,
                                             post_author=user1)

        UserFavoriteMusicians.objects.create(user=user1, musician=musician_1, like=True,
                                             rate=5)
        UserFavoriteMusicians.objects.create(user=user2, musician=musician_1, like=True,
                                             rate=5)
        UserFavoriteMusicians.objects.create(user=user3, musician=musician_1, like=True,
                                             rate=4)

        UserFavoriteMusicians.objects.create(user=user1, musician=musician_2, like=True,
                                             rate=3)
        UserFavoriteMusicians.objects.create(user=user2, musician=musician_2, like=True,
                                             rate=4)
        UserFavoriteMusicians.objects.create(user=user3, musician=musician_2, like=False)

        musicians = Musician.objects.all().annotate(
            annotated_likes=Count(Case(When(userfavoritemusicians__like=True, then=1))),
            rating=Avg('userfavoritemusicians__rate')
        )

        data = MusiciansSerializer(musicians, many=True).data
        expected_data = [
            {
                'id': musician_1.id,
                "first_name": "Aboba 1",
                'post_author': user1.id,
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': 0,
            },
            {
                'id': musician_2.id,
                "first_name": "Aboba 2",
                'post_author': user2.id,
                'likes_count': 2,
                'annotated_likes': 2,
                'rating': 0,
            },
        ]
        self.assertEqual(expected_data, data, 'Invalid data')
