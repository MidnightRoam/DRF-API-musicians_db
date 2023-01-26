from django.urls import reverse
from rest_framework.test import APITestCase
from unittest import TestCase


class MusiciansAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        url = reverse('all-list')
        print(url)
        response = self.client.get(url)
        print(response)
