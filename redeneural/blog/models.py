from auditlog.registry import auditlog

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import AutoSlugField

from redeneural.core.models import AbstractBaseModel


class Category(AbstractBaseModel):

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    slug = AutoSlugField(verbose_name=_('Slug'), max_length=255, populate_from=['title'], unique=True, db_index=True)

    def __str__(self):
        return self.title


class Post(AbstractBaseModel):

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    slug = AutoSlugField(verbose_name=_('Slug'), max_length=255, populate_from=['title'], unique=True, db_index=True)
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.title


auditlog.register(Category)
auditlog.register(Post)
