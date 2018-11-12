from django.contrib import admin
from django.utils.safestring import mark_safe

from redeneural.banner.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'image_thumbnail', 'link']
    list_display_links = ['id', 'link', 'image_thumbnail']

    def image_thumbnail(self, obj):
        html = '<img src="'+obj.image.url+'" class="img-thumbnail col-md-2 p-0"></div>'
        return mark_safe(html)
    image_thumbnail.short_description = 'Imagem'
