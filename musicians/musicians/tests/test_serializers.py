from rest_framework.test import APITestCase

from musicians.serializers import SongsSerializer
from musicians.models import Song


class SongsSerializerTest(APITestCase):
    """Songs serializer tests"""
    def test_ok(self):
        song_1 = Song.objects.create(title="Test song 1", url='1')
        song_2 = Song.objects.create(title="Test song 2", url='2')
        song_3 = Song.objects.create(title="Test song 3", url='3')
        data = SongsSerializer([song_1, song_2, song_3], many=True).data
        expected_data = [
            {
                'id': song_1.id,
                'title': 'Test song 1',
                'url': '1'
            },
            {
                'id': song_2.id,
                'title': 'Test song 2',
                'url': '2'
            },
            {
                'id': song_3.id,
                'title': 'Test song 3',
                'url': '3'
            },
        ]
        self.assertEqual(expected_data, data, 'Invalid data')
