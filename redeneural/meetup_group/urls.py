from django.urls import path

from redeneural.meetup_group import views

app_name = 'meetup_group'

urlpatterns = [
    path('', views.index, name='home'),
]
