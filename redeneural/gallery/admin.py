from django.contrib import admin
from django.utils.safestring import mark_safe

from redeneural.gallery.models import EventImage


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['event', 'image_thumbnail']
    list_display_links = ['event']

    def image_thumbnail(self, obj):
        html = '<img src="'+obj.image.url+'" class="img-thumbnail col-md-2 p-0"></div>'
        return mark_safe(html)
    image_thumbnail.short_description = 'Imagem'
