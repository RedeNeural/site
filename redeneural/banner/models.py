from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _

from redeneural.storage import get_storage_path
from redeneural.core.models import AbstractBaseModel


def get_banner_path(instance, filename):
    return get_storage_path(filename, 'banners')


class Banner(AbstractBaseModel):

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

    image = models.ImageField(upload_to=get_banner_path, verbose_name=_('Image'))
    link = models.URLField(verbose_name='Link', null=True, blank=True)

    def __str__(self):
        return str(self.id)


auditlog.register(Banner)
