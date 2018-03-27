from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from randomslugfield import RandomSlugField
from accounts.models import Account
from contacts.models import Contact


class List(models.Model):
    ugid = RandomSlugField(length=7, unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='uuid')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    assigned_contacts = models.ManyToManyField(Contact, related_name='assigned_contacts_list', blank=True)

    class Meta:
        verbose_name = _('List')
        verbose_name_plural = _('Lists')

    def __str__(self):
        return self.title
