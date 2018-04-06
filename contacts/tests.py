import datetime

from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from accounts.models import Account
from . import models


class ContactTest(APITestCase):
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

        self.test_contact = models.Contact(
            account=self.test_account,
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )
        self.test_contact.save()
        self.create_url = reverse('contacts:contact_create')
        self.list_url = reverse('contacts:contact_list', kwargs={'account': self.test_account.uaid})
        self.retrieve_url = reverse('contacts:contact_rud',
                                    kwargs={
                                        'ucid': self.test_contact.ucid,
                                        'account': self.test_account.uaid,
                                    })

    def test_create_contact(self):
        """
        Ensure we can create a new Contact.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )

        data = {
            'account': self.test_account.uaid,
            'first_name': 'foo',
            'last_name': 'bar',
        }

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(models.Contact.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertTrue('last_name' in response.data)

    def test_list_contacts(self):
        """
        Ensure we can list the Contacts of a user.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }
        response = self.client.get(self.list_url, format='json', **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_contact(self):
        """
        Ensure we can retrieve a Contact.
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

    def test_update_contact(self):
        """
        Ensure we can update a Contact.
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
            'first_name': 'Jane',
            'last_name': 'Doe',
        }

        response = self.client.put(self.retrieve_url, data, format='json', **auth_headers)
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_contact(self):
        """
        Ensure we can delete a Contact.
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
