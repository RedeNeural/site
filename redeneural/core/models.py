from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from redeneural.core.signals import post_soft_delete
from redeneural.core.manager import Manager


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
    deleted_at = models.DateTimeField(verbose_name=_('Deleted at'), null=True, blank=True)
    objects = Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        post_soft_delete.send(sender=type(self), instance=self, using=self._state.db)


class About(AbstractBaseModel):

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')

    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.content
