from rest_framework.test import APITestCase

from musicians.serializers import SongsSerializer
from musicians.models import Song


class SongsSerializerTest(APITestCase):
    """Songs serializer tests"""
    def test_ok(self):
        song_1 = Song.objects.create(title="test", url='1')
        song_2 = Song.objects.create(title="test2", url='2')
        data = SongsSerializer([song_1, song_2], many=True).data
        expected_data = [
            {
                'id': song_1.id,
                'title': 'test',
                'url': '1'
            },
            {
                'id': song_2.id,
                'title': 'test2',
                'url': '2'
            },
        ]
        self.assertEqual(expected_data, data, 'Invalid data')
