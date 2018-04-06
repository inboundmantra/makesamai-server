import datetime

from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from . import models


class AccountTest(APITestCase):
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
        self.test_account = models.Account(owner=self.test_user, name='test', domain='http://www.example.com')
        self.test_account.save()
        self.create_url = reverse('accounts:list_create')
        self.retrieve_url = reverse('accounts:retrieve', kwargs={'uaid': self.test_account.uaid})

    def test_create_account(self):
        """
        Ensure we can create a new Account.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )

        data = {
            'owner': self.test_user.uuid,
            'name': 'foo bar',
            'domain': 'http://www.foobar.com',
        }

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(models.Account.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertTrue('domain' in response.data)

    def test_create_account_with_no_domain(self):
        """
        Ensure we can create a new Account without domain data.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        data = {
            'owner': self.test_user.uuid,
            'name': 'foo bar',
        }
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }
        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Account.objects.count(), 2)
        self.assertEqual(response.data['domain'], None)

    def test_list_user_accounts(self):
        """
        Ensure we can list the Accounts of a user.
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

    def test_retrieve_account(self):
        """
        Ensure we can retrieve an Account.
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

    def test_update_account(self):
        """
        Ensure we can update an Account.
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
            'owner': self.test_user.uuid,
            'uaid': self.test_account.uaid,
            'name': 'foo bar',
            'domain': 'http://www.foobarexample.com'
        }

        response = self.client.put(self.retrieve_url, data, format='json', **auth_headers)
        self.assertEqual(response.data['domain'], data['domain'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        """
        Ensure we can delete an Account.
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
