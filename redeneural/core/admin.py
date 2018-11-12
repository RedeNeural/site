from django.contrib import admin
from django.shortcuts import redirect
from django_summernote.admin import SummernoteModelAdmin

from redeneural.core.models import About


def redirect_one_object(model, obj):
    response = redirect(f'/admin/{model._meta.app_label}/{model._meta.model_name}/add/')
    if obj:
        response = redirect(f'/admin/{model._meta.app_label}/{model._meta.model_name}/{obj.pk}/change/')

    return response


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    exclude = ['deleted_at']
    list_display = ['content']
    list_display_links = ['content']
    summernote_fields = ['content']

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.first():
            return redirect_one_object(self.model, self.model.objects.first())
        return super().add_view(request, form_url='', extra_context=None)

    def changelist_view(self, request, extra_context=None):
        return redirect_one_object(self.model, self.model.objects.first())
