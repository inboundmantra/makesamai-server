from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from randomslugfield import RandomSlugField
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from lists.models import List
import logging

logger = logging.getLogger(__name__)


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

    def __str__(self):
        return self.campaign_title


class Email(models.Model):
    umid = RandomSlugField(length=9, unique=True, primary_key=True)
    campaign = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE, to_field='cmid', blank=True, null=True)
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

    def send_email_campaign(sender, instance, created, **kwargs):
        if created:
            for contact in instance.list.assigned_contacts.all():
                try:
                    Email.objects.create(
                        campaign=instance,
                        account=instance.account,
                        to_email=contact.email,
                        subject=instance.subject,
                        message=instance.message_template
                    )
                except:
                    logger.error('Mail Send Error: ', exc_info=True)
                finally:
                    pass

    post_save.connect(send_email_campaign, sender=EmailCampaign)

    def create(self):
        self.save()

    def __str__(self):
        return self.to_email
