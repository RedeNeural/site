from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import AutoSlugField

from redeneural.core.models import AbstractBaseModel
from redeneural.storage import get_storage_path


def get_event_path(instance, filename):
    return get_storage_path(filename, 'event')


class Event(AbstractBaseModel):

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = AutoSlugField(verbose_name=_('Slug'), max_length=255, populate_from=['name'], unique=True, db_index=True)

    short_description = models.TextField(verbose_name=_('Short Description'))
    long_description = models.TextField(verbose_name=_('Long Description'))

    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))

    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(verbose_name=_('End Time'))

    location = models.CharField(verbose_name=_('Location'), max_length=500)

    image = models.ImageField(upload_to=get_event_path, verbose_name=_('Image'), null=True, blank=True)

    limit_participants = models.PositiveIntegerField(verbose_name=_('Limit Participants'), default=0)

    is_active = models.BooleanField(verbose_name=_('Active?'), default=False)

    def __str__(self):
        return self.name
