from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from randomslugfield import RandomSlugField

from accounts.models import Account


class Form(models.Model):
    ufid = RandomSlugField(length=7, unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='uuid')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    title_enabled = models.BooleanField(default=False)
    title_required = models.BooleanField(default=False)

    fname_enabled = models.BooleanField(default=True)
    fname_required = models.BooleanField(default=False)

    lname_enabled = models.BooleanField(default=True)
    lname_required = models.BooleanField(default=False)

    email_enabled = models.BooleanField(default=True)
    email_required = models.BooleanField(default=True)

    company_enabled = models.BooleanField(default=False)
    company_required = models.BooleanField(default=False)

    website_enabled = models.BooleanField(default=False)
    website_required = models.BooleanField(default=False)

    phone_enabled = models.BooleanField(default=False)
    phone_required = models.BooleanField(default=False)

    address_line_enabled = models.BooleanField(default=False)
    address_line_required = models.BooleanField(default=False)

    street_enabled = models.BooleanField(default=False)
    street_required = models.BooleanField(default=False)

    city_enabled = models.BooleanField(default=False)
    city_required = models.BooleanField(default=False)

    state_enabled = models.BooleanField(default=False)
    state_required = models.BooleanField(default=False)

    postcode_enabled = models.BooleanField(default=False)
    postcode_required = models.BooleanField(default=False)

    country_enabled = models.BooleanField(default=False)
    country_required = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Form')
        verbose_name_plural = _('Forms')

    def __str__(self):
        return self.title
