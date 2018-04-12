import datetime

from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from accounts.models import Account
from forms.models import Form
from . import models


class LandingPageTest(APITestCase):
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

        self.test_form = Form(
            account=self.test_account,
            created_by=self.test_user,
            title="Foo Form"
        )
        self.test_form.save()
        self.test_lp = models.LandingPage(
            account=self.test_account,
            created_by=self.test_user,
            title="Foo LP",
            slug="foo-lp",
            form=self.test_form
        )
        self.test_lp.save()
        self.create_url = reverse('landing_pages:list_create', kwargs={'account': self.test_account.uaid})
        self.retrieve_url = reverse('landing_pages:retrieve_update_delete',
                                    kwargs={
                                        'ulid': self.test_lp.ulid,
                                        'account': self.test_account.uaid,
                                    })
        self.render_url = reverse('landing_pages:render',
                                  kwargs={
                                      'slug': self.test_lp.slug,
                                      'account': self.test_account.uaid,
                                  })

    def test_create_lp(self):
        """
        Ensure we can create a new Landing Page.
        """
        tok = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application, scope='read write',
            expires=timezone.now() + datetime.timedelta(days=1)
        )

        data = {
            'account': self.test_account.uaid,
            'created_by': self.test_user.uuid,
            'title': 'Bar LP',
            'slug': "bar-lp",
            'form': self.test_form.ufid,
        }

        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + tok.token,
        }

        response = self.client.post(self.create_url, data, format='json', **auth_headers)
        self.assertEqual(models.LandingPage.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertTrue('ulid' in response.data)

    def test_list_lp(self):
        """
        Ensure we can list the Landing Pages of an user.
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

    def test_retrieve_lp(self):
        """
        Ensure we can retrieve a Landing Page.
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

    def test_update_lp(self):
        """
        Ensure we can update a Landing Page.
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
            'title': 'Foo Bar LP',
            'slug': "foo-bar-lp",
            'form': self.test_form.ufid,
        }

        response = self.client.put(self.retrieve_url, data, format='json', **auth_headers)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_render_lp(self):
        """
        Ensure we can render a Landing Page.
        """
        response = self.client.get(self.render_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lp(self):
        """
        Ensure we can delete a Landing Page.
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
