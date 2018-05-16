from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from randomslugfield import RandomSlugField
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from lists.models import List


class Email(models.Model):
    umid = RandomSlugField(length=9, unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid')
    to_email = models.EmailField(max_length=200)
    from_email = models.EmailField(max_length=200, default='no-reply@makesamai.com')
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, default='SENT')

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def save(self, *args, **kwargs):
        email = EmailMessage(
            self.subject,
            self.message,
            self.from_email,
            [self.to_email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject


class EmailCampaign(models.Model):
    cmid = RandomSlugField(length=9, unique=True, primary_key=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='uuid', on_delete=models.CASCADE, blank=True,
                                   null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid')
    list = models.ForeignKey(List, on_delete=models.CASCADE, to_field='ugid', blank=True, null=True)
    campaign_title = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message_template = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')

    def save(self, *args, **kwargs):
        # for contact in self.list.assigned_contacts:
        #     email = EmailMessage(
        #         self.subject,
        #         self.message_template,
        #         'no-reply@makesamai.com',
        #         [contact.email],
        #     )
        #     email.content_subtype = "html"
        #     email.send(fail_silently=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.campaign_title
