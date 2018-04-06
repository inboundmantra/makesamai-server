import datetime

from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from accounts.models import Account
from . import models


class ListTest(APITestCase):
    def setUp(self):
        self.test_user = Client.objects.create_user('test', 'user', 'test@example.com',
                                                    'testpassword')
        self.application = Application(
            name="Test Application",
            redirect_uris="http://localhost",
            user=self.test_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        )
        self.application.save()
        self.test_account = Account(owner=self.test_user, name='test', domain='http://www.example.com')
        self.test_account.save()

        self.test_list = models.List(
            account=self.test_account,
            created_by=self.test_user,
            title="Foo List"
        )
        self.test_list.save()
        self.create_url = reverse('lists:list_create', kwargs={'account': self.test_account.uaid})
        self.retrieve_url = reverse('lists:retrieve_update_delete',
                                    kwargs={
                                        'ugid': self.test_list.ugid,
                                        'account': self.test_account.uaid,
                                    })

    def test_create_list(self):
        """
        Ensure we can create a new List.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )

        data = {
            'account': self.test_account.uaid,
            'created_by': self.test_user.uuid,
            'title': 'Bar List',
        }

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(models.List.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertTrue('ugid' in response.data)

    def test_list_lists(self):
        """
        Ensure we can list the Lists of a user.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }
        response = self.client.get(self.create_url, format='json', **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_list(self):
        """
        Ensure we can retrieve a List.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }
        response = self.client.get(self.retrieve_url, format='json', **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_list(self):
        """
        Ensure we can update an List.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        data = {
            'account': self.test_account.uaid,
            'created_by': self.test_user.uuid,
            'title': 'Foo Bar List',
        }

        response = self.client.put(self.retrieve_url, data, format='json', **auth_headers)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_list(self):
        """
        Ensure we can delete an List.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.delete(self.retrieve_url, format='json', **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
