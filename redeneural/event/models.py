from auditlog.registry import auditlog

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from redeneural.core.models import AbstractBaseModel
from redeneural.storage import get_storage_path


def get_event_path(instance, filename):
    return get_storage_path(filename, 'event/image')


def get_banner_path(instance, filename):
    return get_storage_path(filename, 'event/banner')


class EventManager(models.Manager):

    def get_next_event(self):
        queryset = self.get_queryset().filter(is_active=True)
        return queryset.order_by('start_date').first()


class Event(AbstractBaseModel):

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    objects = EventManager()

    meetup_group = models.ForeignKey('meetup_group.MeetupGroup', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, db_index=True)

    long_description = models.TextField(verbose_name=_('Long Description'))
    short_description = models.TextField(verbose_name=_('Short Description'), null=True, blank=True)

    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    start_time = models.TimeField(verbose_name=_('Start Time'), null=True, blank=True)
    end_time = models.TimeField(verbose_name=_('End Time'), null=True, blank=True)

    location = models.CharField(verbose_name=_('Location'), max_length=500)

    image = models.ImageField(upload_to=get_event_path, verbose_name=_('Image'), null=True, blank=True)
    banner = models.ImageField(upload_to=get_banner_path, verbose_name=_('Banner'), null=True, blank=True)

    # Control event
    limit_participants = models.PositiveIntegerField(verbose_name=_('Limit Participants'), default=0)
    open_subscriptions_on = models.DateTimeField(verbose_name=_('Abrir inscrições em?'), default=timezone.now)
    close_subscriptions_on = models.DateTimeField(verbose_name=_('Encerrar inscrições em?'), default=timezone.now)
    is_active = models.BooleanField(verbose_name=_('Active?'), default=False)

    def __str__(self):
        return self.name


auditlog.register(Event)
