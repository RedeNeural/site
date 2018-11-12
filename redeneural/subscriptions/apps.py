from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SubscriptionsConfig(AppConfig):

    name = 'redeneural.subscriptions'
    verbose_name = _('Subscription')
    verbose_name_plural = _('Subscriptions')
