from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from forms.models import Form


class LandingPage(models.Model):
    """
    Landing Page Model.
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', related_name='lp_created_by',
                                   on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField()
    description = models.TextField(_('Description'), blank=True, null=True)
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    brand_name = models.CharField(_('Brand Name'), max_length=255, default='Brand Name')
    form = models.ForeignKey(Form, to_field='title', related_name='lp_form')
    thank_you_message = models.TextField(default="Your Response Has Been Recorded, Thank You For Submitting the Form!")

    class Meta:
        verbose_name = _('Landing Page')
        verbose_name_plural = _('Landing Pages')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
