from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from randomslugfield import RandomSlugField

from . import managers


class Client(AbstractBaseUser, PermissionsMixin):
    """
    A Custom User model with admin-compliant Permissions.
    First Name, Last Name, and Email are required.
    """
    email = models.EmailField(_('Email Address'), max_length=254, unique=True)
    uuid = RandomSlugField(length=7, unique=True, primary_key=True)
    first_name = models.CharField(_('First Name'), max_length=30)
    last_name = models.CharField(_('Last Name'), max_length=30)
    is_staff = models.BooleanField(_('Staff Status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text='Designates whether this user should be treated as'
                                              'active. Unselect this instead of deleting accounts')
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)
    objects = managers.ClientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/api/client/%d/" % urlquote(self.id)

    def get_full_name(self):
        """
        Full Name.
        :return: Returns the first_name plus the last_name, with space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Short Name.
        :return: Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        :param subject: Subject of the mail.
        :param message:  Message content of the mail.
        :param from_email: the senders email.
        """
        send_mail(subject, message, from_email, [self.email])
