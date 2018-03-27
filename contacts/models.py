from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from randomslugfield import RandomSlugField

from MakeSamai.utils import TITLE, COUNTRIES, LIFECYCLE_STATUS, STAGES
from accounts.models import Account
from forms.models import Form
from landing_pages.models import LandingPage


class Address(models.Model):
    """
    Address Model.
    """
    address_line = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    street = models.CharField(_("Street"), max_length=55, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    postcode = models.CharField(_("Post/Zip-code"), max_length=64, blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Contact(models.Model):
    """
    Contact Model.
    """
    ucid = RandomSlugField(length=10, unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid')
    form = models.ForeignKey(Form, on_delete=models.CASCADE, to_field='ufid', blank=True, null=True)
    landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE, to_field='ulid', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='uuid', related_name='created_by',
                                   on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=3, choices=TITLE, blank=True, null=True)
    first_name = models.CharField(_("First name"), max_length=255, default=" ", blank=True)
    last_name = models.CharField(_("Last name"), max_length=255, default=" ", blank=True)
    email = models.EmailField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Address, related_name='address', on_delete=models.CASCADE, blank=True,
                                null=True)
    status = models.CharField(_('Status'), max_length=50, choices=LIFECYCLE_STATUS, default='lead', blank=True,
                              null=True)
    stage = models.CharField(_('Stage'), max_length=50, choices=STAGES, default='lead', blank=True,
                             null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    @property
    def get_full_name(self):
        """
        Full Name
        :return: Returns the first_name plus the last_name, with space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_short_name(self):
        """
        Short Name
        :return: Returns the first_name.
        """
        short_name = "%s" % self.first_name
        return short_name.strip()

    def __str__(self):
        return str(self.get_full_name)
