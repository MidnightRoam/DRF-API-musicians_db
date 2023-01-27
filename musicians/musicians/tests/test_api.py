from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from musicians.models import Song
from musicians.serializers import SongsSerializer


class SongAPITestCase(APITestCase):
    """Song API tests"""
    def setUp(self):
        self.song_1 = Song.objects.create(title="Test song MGK", url='1')
        self.song_2 = Song.objects.create(title="Test song Rock", url='2')
        self.song_3 = Song.objects.create(title="Test song MGK", url='3')
        self.song_4 = Song.objects.create(title="Rock", url='4')

    def test_get(self):
        """Get songs test"""
        url = reverse('musicians:songs-list')
        response = self.client.get(url)
        serializer_data = SongsSerializer([self.song_1, self.song_2, self.song_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        self.assertEqual(serializer_data, response.data)  # check if data is correct

    def test_get_filter(self):
        """Filter songs test"""
        url = reverse('musicians:songs-list')
        response = self.client.get(url, data={'title': 'Rock'})
        print(response.data)
        serializer_data = SongsSerializer([self.song_1,
                                           self.song_4], many=True).data
        print(f'Serializer data: {serializer_data}')
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        self.assertEqual(serializer_data, response.data)  # check if data is correct

    def test_get_search(self):
        """Searching songs test"""
        url = reverse('musicians:songs-list')
        response = self.client.get(url, data={'search': 'Rock'})
        serializer_data = SongsSerializer([self.song_2,
                                           self.song_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        self.assertEqual(serializer_data, response.data)  # check if data is correct

    def test_get_order(self):
        """Order songs test"""
        url = reverse('musicians:songs-list')
        response = self.client.get(url, data={'order': 'title'})
        serializer_data = SongsSerializer([self.song_1,
                                           self.song_2,
                                           self.song_3,
                                           self.song_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200 OK"
        self.assertEqual(serializer_data, response.data)  # check if data is correct