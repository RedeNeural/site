from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _

from redeneural.core.models import AbstractBaseModel


class Category(AbstractBaseModel):

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        unique_together = (
            ('meetup_group', 'slug')
        )

    meetup_group = models.ForeignKey('meetup_group.MeetupGroup', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, db_index=True)

    def __str__(self):
        return self.title


class Post(AbstractBaseModel):

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    meetup_group = models.ForeignKey('meetup_group.MeetupGroup', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, db_index=True)
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.title


auditlog.register(Category)
auditlog.register(Post)
