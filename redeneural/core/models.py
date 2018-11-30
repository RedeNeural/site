from uuid import uuid4

from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(verbose_name='UUID', default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)


class About(AbstractBaseModel):

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')

    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.content


auditlog.register(About)
