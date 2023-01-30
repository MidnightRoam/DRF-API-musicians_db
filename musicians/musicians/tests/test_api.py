import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from musicians.models import Song, Musician, UserFavoriteMusicians
from musicians.serializers import SongsSerializer, MusiciansSerializer


class SongAPITestCase(APITestCase):
    """Song API tests"""

    def setUp(self):
        self.song_1 = Song.objects.create(title="Test song MGK", url='http://test-url1.com')
        self.song_2 = Song.objects.create(title="Test song Rock", url='http://test-url2.com')
        self.song_3 = Song.objects.create(title="Test song MGK", url='http://test-url3.com')
        self.song_4 = Song.objects.create(title="Rock", url='http://test-url4.com')
        self.user_staff = User.objects.create(username='test_admin', is_staff=True)
        self.user = User.objects.create(username='test_user')

    def test_get(self):
        """Get songs test"""
        url = reverse('musicians:songs-list')
        response = self.client.get(url)
        serializer_data = SongsSerializer([self.song_1, self.song_2, self.song_3, self.song_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        self.assertEqual(serializer_data, response.data)  # check if data is correct

    def test_get_detail(self):
        """Get detail song test"""
        url = reverse('musicians:songs-detail', args=(self.song_1.id,))
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"

    # def test_get_filter(self):
    #     """Filter songs test"""
    #     url = reverse('musicians:songs-list')
    #     response = self.client.get(url, data={'title': 'MGK'})
    #     print(response.data)
    #     serializer_data = SongsSerializer([self.song_1,
    #                                        self.song_3], many=True).data
    #     print(f'Serializer data: {serializer_data}')
    #     print(f'Сериалайзер дата: {serializer_data}')
    #     print(f'Респонс дата: {response.data}')
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
    #     self.assertEqual(serializer_data, response.data)  # check if data is correct

    # def test_get_search(self):
    #     """Searching songs test"""
    #     url = reverse('musicians:songs-list')
    #     response = self.client.get(url, data={'search': 'Rock'})
    #     serializer_data = SongsSerializer([self.song_2,
    #                                        self.song_4], many=True).data
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
    #     self.assertEqual(serializer_data, response.data)  # check if data is correct

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

    def test_create(self):
        """Create songs test"""
        self.assertEqual(4, Song.objects.all().count())  # Check that we have 4 songs in database
        url = reverse('musicians:songs-list')
        data = {
            'title': 'test song',
            'url': 'http://testurl.com'
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user_staff)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)  # check if status code is "201"
        self.assertEqual(5, Song.objects.all().count())  # Check that amount of songs in database increased by 1

    def test_update(self):
        """Update songs test"""
        url = reverse('musicians:songs-detail', args=(self.song_1.id,))
        data = {
            'title': self.song_1.title,
            'url': "http://new-test-url1.com",
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user_staff)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        self.song_1.refresh_from_db()
        self.assertEqual("http://new-test-url1.com", self.song_1.url)

    def test_update_not_admin(self):
        """Update song if user not staff test"""
        url = reverse('musicians:songs-detail', args=(self.song_1.id,))
        data = {
            'title': self.song_1.title,
            'url': "http://new-test-url1.com",
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)  # check if status code is "200"
        self.song_1.refresh_from_db()
        self.assertEqual(self.song_1.url, "http://test-url1.com")

    def test_delete(self):
        """Delete songs test"""
        url = reverse('musicians:songs-detail', args=(self.song_1.id,))
        self.client.force_login(self.user_staff)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)  # check if status code is "200"
        self.assertEqual(3, Song.objects.all().count())  # check that song was decresead by 1 in db

    def test_delete_not_admin(self):
        """Delete songs if user not staff test"""
        url = reverse('musicians:songs-detail', args=(self.song_1.id,))
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(4, Song.objects.all().count())


class MusicianAPITestCase(APITestCase):
    """Musicians API tests"""

    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.musician_1 = Musician.objects.create(first_name="Test Musician 1",
                                                  age=18,
                                                  post_author=self.user),
        self.musician_2 = Musician.objects.create(first_name="Test Musician 2",
                                                  age=18,
                                                  post_author=self.user)

    # def test_get(self):
    #     """Get list of musicians test"""
    #     url = reverse('musicians:all-list')
    #     response = self.client.get(url)
    #     serializer_data = MusiciansSerializer([self.musician_1, self.musician_2], many=True).data
    #     print(f'1 {response.data}')
    #     print(f'2 {serializer_data}')
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
    #     self.assertEqual(serializer_data, response.data)  # check if data is correct
    #
    # def test_get_detail(self):
    #     """Get detail of musician test"""
    #     url = reverse('musicians:all-detail', args=(self.musician_1.id,))
    #     response = self.client.get(url)
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"

    # def test_update(self):
    #     """Update musicians test"""
    #     url = reverse('musicians:all-detail', args=(self.musician_1.id,))
    #     data = {
    #         'first_name': 'Abobes'
    #     }
    #     json_data = json.dumps(data)
    #     self.client.force_login(self.user)
    #     response = self.client.put(url, data=json_data, content_type='application/json')
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
    #     self.musician_1.refresh_from_db()
    #     self.assertEqual("http://new-test-url1.com", self.musician_1.url)


class MusicianRelationTestCase(APITestCase):
    """Musician - user relation API tests"""

    def setUp(self):
        self.user_staff = User.objects.create(username='test_admin', is_staff=True)
        self.user = User.objects.create(username='test_user')
        self.musician_1 = Musician.objects.create(first_name="Aboba 1",
                                                  age=18,
                                                  post_author=self.user_staff)
        self.musician_2 = Musician.objects.create(first_name="Aboba 2",
                                                  age=20,
                                                  post_author=self.user)

    def test_like(self):
        """Like musician test"""
        url = reverse('musicians:rate-detail', args=(self.musician_1.id,))
        data = {
            'like': True,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        relation = UserFavoriteMusicians.objects.get(user=self.user,
                                                     musician=self.musician_1)
        self.assertTrue(relation.like)

        data = {
            'in_favorite': True,
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        relation = UserFavoriteMusicians.objects.get(user=self.user,
                                                     musician=self.musician_1)
        self.assertTrue(relation.in_favorite)

    def test_rate(self):
        """Rate musician test"""
        url = reverse('musicians:rate-detail', args=(self.musician_1.id,))
        data = {
            'rate': 5,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # check if status code is "200"
        relation = UserFavoriteMusicians.objects.get(user=self.user,
                                                     musician=self.musician_1)
        self.assertEqual(5, relation.rate)

    def test_rate_wrong(self):
        """Wrong rate musician test"""
        url = reverse('musicians:rate-detail', args=(self.musician_1.id,))
        data = {
            'rate': 6,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code, response.data)  # check if status code is "200"