from django.contrib import admin
from redeneural.subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['name', 'email']
    list_display_links = ['name', 'email']
