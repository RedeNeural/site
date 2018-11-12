from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from redeneural.event.models import Event


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    exclude = ['deleted_at']
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    summernote_fields = ['short_description', 'long_description']
