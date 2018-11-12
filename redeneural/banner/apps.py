from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BannerConfig(AppConfig):

    name = 'redeneural.banner'
    verbose_name = _('Banner')
    verbose_name_plural = _('Banners')
