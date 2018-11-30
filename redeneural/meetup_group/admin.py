from django.contrib import admin

from redeneural.meetup_group.models import MeetupGroup


@admin.register(MeetupGroup)
class MeetupGroupAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
