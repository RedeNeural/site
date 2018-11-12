from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from redeneural.event.models import Event
from redeneural.gallery.models import EventImage


class EventImageInline(admin.TabularInline):

    exclude = ['deleted_at']
    model = EventImage
    extra = 3


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    exclude = ['deleted_at']
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    summernote_fields = ['short_description', 'long_description']
    inlines = [
        EventImageInline
    ]
