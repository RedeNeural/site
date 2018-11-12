from django.urls import path

from redeneural.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
