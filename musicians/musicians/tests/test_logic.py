from unittest import TestCase
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from musicians.logic import set_rating
from musicians.models import Musician, UserFavoriteMusicians


class SetRatingTestCase(APITestCase):
    """Musician rating tests"""

    def setUp(self):
        """Set up for tests"""
        user1 = User.objects.create(username='test_user1', is_staff=True)
        user2 = User.objects.create(username='test_user2')
        user3 = User.objects.create(username='test_user3')

        self.musician_1 = Musician.objects.create(first_name="Aboba 1",
                                                  age=18,
                                                  post_author=user1)

        UserFavoriteMusicians.objects.create(user=user1, musician=self.musician_1, like=True,
                                             rate=5)
        UserFavoriteMusicians.objects.create(user=user2, musician=self.musician_1, like=True,
                                             rate=5)
        UserFavoriteMusicians.objects.create(user=user3, musician=self.musician_1, like=True,
                                             rate=4)

    def test_ok(self):
        """Test ok test"""
        set_rating(self.musician_1)
        self.musician_1.refresh_from_db()
        self.assertEqual('4.67', str(self.musician_1.rating))
