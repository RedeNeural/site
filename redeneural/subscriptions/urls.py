from django.urls import path

from redeneural.subscriptions import views

app_name = 'subscriptions'

urlpatterns = [
    path('<slug:event_slug>', views.form, name='form'),
]
