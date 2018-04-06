from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class UserCreateTest(APITestCase):
    def setUp(self):
        self.test_user = models.Client.objects.create_user('test', 'user', 'test@example.com',
                                                           'testpassword')

        self.create_url = reverse('clients:create')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(models.Client.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_no_password(self):
        data = {
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foobarbaz@example.com',
            'password': ''
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(models.Client.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)
