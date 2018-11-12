from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _

from redeneural.core.models import AbstractBaseModel


class Subscription(AbstractBaseModel):

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
        unique_together = (
            ('event', 'email')
        )

    event = models.ForeignKey('event.Event', verbose_name=_('Event'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    email = models.EmailField(verbose_name=_('Email'), max_length=255)

    def __str__(self):
        return self.name


auditlog.register(Subscription)
