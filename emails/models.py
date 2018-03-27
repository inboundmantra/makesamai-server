from django.core.mail import EmailMessage
from django.db import models
from randomslugfield import RandomSlugField
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account


class Email(models.Model):
    umid = RandomSlugField(length=9, unique=True, primary_key=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='uaid', editable=False)
    to_email = models.EmailField(max_length=200, editable=False)
    from_email = models.EmailField(max_length=200, default='no-reply@makesamai.com', editable=False)
    subject = models.CharField(max_length=255, blank=True, null=True, editable=False)
    message = models.TextField(blank=True, null=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
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
