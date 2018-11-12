from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from redeneural.blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    exclude = ['deleted_at']
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    exclude = ['deleted_at']
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    summernote_fields = ['content']
