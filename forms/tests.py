import datetime

from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from accounts.models import Account
from . import models


class FormTest(APITestCase):
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

        self.test_form = models.Form(
            account=self.test_account,
            created_by=self.test_user,
            title="Foo Form"
        )
        self.test_form.save()
        self.create_url = reverse('forms:list_create', kwargs={'account': self.test_account.uaid})
        self.retrieve_url = reverse('forms:retrieve_update_delete',
                                    kwargs={
                                        'ufid': self.test_form.ufid,
                                        'account': self.test_account.uaid,
                                    })
        self.render_url = reverse('forms:render',
                                  kwargs={
                                      'ufid': self.test_form.ufid,
                                      'account': self.test_account.uaid,
                                  })

    def test_create_form(self):
        """
        Ensure we can create a new Form.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )

        data = {
            'account': self.test_account.uaid,
            'created_by': self.test_user.uuid,
            'title': 'Bar Form',
        }

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(models.Form.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertTrue('ufid' in response.data)

    def test_list_forms(self):
        """
        Ensure we can list the Forms of an user.
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

    def test_retrieve_form(self):
        """
        Ensure we can retrieve a Form.
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
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_form(self):
        """
        Ensure we can update a Form.
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
            'title': 'Foo Bar Form',
        }

        response = self.client.put(self.retrieve_url, data, format='json', **auth_headers)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_render_form(self):
        """
        Ensure we can render a Form.
        """
        response = self.client.get(self.render_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_form(self):
        """
        Ensure we can delete a Form.
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
