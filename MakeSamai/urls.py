"""MakeSamai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
                  path('/', admin.site.urls),
                  path('', include('clients.urls', namespace='clients')),
                  path('', include('accounts.urls', namespace='accounts')),
                  path('', include('contacts.urls', namespace='contacts')),
                  path('', include('forms.urls', namespace='forms')),
                  path('', include('landing_pages.urls', namespace='landing_pages')),
                  url(r'^accounts/login/$', django.contrib.auth.views.login, {'template_name': 'admin/login.html'},
                      name="login"),
                  url(r'^api-auth/', include('rest_framework.urls',
                                             namespace='rest_framework')),
                  url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
