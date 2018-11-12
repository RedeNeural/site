from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EventConfig(AppConfig):

    name = 'redeneural.event'
    verbose_name = _('Event')
    verbose_name_plural = _('Events')
