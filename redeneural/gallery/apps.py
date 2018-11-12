from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GalleryConfig(AppConfig):

    name = 'redeneural.gallery'
    verbose_name = _('Gallery')
    verbose_name_plural = _('Galleries')
