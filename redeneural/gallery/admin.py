from django.contrib import admin

from redeneural.gallery.models import EventImage


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['event']
    list_display_links = ['event']

