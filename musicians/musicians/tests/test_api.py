from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from musicians.models import Song
from musicians.serializers import SongsSerializer


class SongAPITestCase(APITestCase):
    """Song API tests"""
    def setUp(self):
        pass

    def test_get(self):
        song_1 = Song.objects.create(title="test", url='1')
        song_2 = Song.objects.create(title="test2", url='2')

        url = reverse('musicians:songs-list')
        response = self.client.get(url)
        serializer_data = SongsSerializer([song_1, song_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200 OK"
        self.assertEqual(serializer_data, response.data)  # check if data is correct
