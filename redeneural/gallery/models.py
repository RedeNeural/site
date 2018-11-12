from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _

from redeneural.storage import get_storage_path
from redeneural.core.models import AbstractBaseModel


def get_image_path(instance, filename):
    return get_storage_path(filename, 'image')


class EventImage(AbstractBaseModel):

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    event = models.ForeignKey('event.Event', verbose_name=_('Event'), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, verbose_name=_('Image'))

    def __str__(self):
        return f'{self.event.name} - {str(self.id)}'


auditlog.register(EventImage)
