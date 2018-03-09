from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote

from randomslugfield import RandomSlugField
from django.utils.translation import ugettext_lazy as _
from . import managers


class Account(models.Model):
    uaid = RandomSlugField(length=7, unique=True, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='uuid')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    objects = managers.AccountManager()

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def get_absolute_url(self):
        return "/api/account/%s/" % urlquote(self.uid)

    def __str__(self):
        return self.name
