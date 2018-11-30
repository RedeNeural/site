from django.db import models
from django.utils.translation import ugettext_lazy as _

from redeneural.storage import get_storage_path
from redeneural.core.models import AbstractBaseModel


def get_meetup_group_image_path(instance, filename):
    return get_storage_path(filename, 'meetup_group/image')


def get_meetup_group_cover_path(instance, filename):
    return get_storage_path(filename, 'meetup_group/cover')


class MeetupGroup(AbstractBaseModel):

    class Meta:
        verbose_name = _('Meetup Group')
        verbose_name_plural = _('Meetup Groups')

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to=get_meetup_group_image_path, verbose_name=_('Image'), null=True, blank=True)
    cover_image = models.ImageField(upload_to=get_meetup_group_cover_path, verbose_name=_('Cover Image'), null=True,
                                    blank=True)

    def __str__(self):
        return self.name
