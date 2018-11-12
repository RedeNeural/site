from django.apps import AppConfig
from auditlog.apps import AuditlogConfig
from suit.apps import DjangoSuitConfig
from django.utils.translation import ugettext_lazy as _


class AuditlogCustomConfig(AuditlogConfig):

    verbose_name = _('Auditing')


class CoreConfig(AppConfig):

    name = 'redeneural.core'
    verbose_name = _('Management')
    verbose_name_plural = _('Management')


class SuitConfig(DjangoSuitConfig):

    layout = 'vertical'
