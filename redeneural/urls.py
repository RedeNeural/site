"""redeneural URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include
from django.conf.urls.static import static


# Admin customization.
admin.site.site_header = 'Rede Neural'
admin.site.site_title = 'Rede Neural'
admin.site.index_title = 'Administração'


urlpatterns = [
    path('admin/', admin.site.urls),

    # Summernote
    path('summernote/', include('django_summernote.urls')),

    # Subscription
    path('eventos/', include('redeneural.subscriptions.urls', namespace='subscriptions')),

    # Home
    path('', include('redeneural.core.urls', namespace='core')),

    # Meetup_group
    path('grupos/', include('redeneural.meetup_group.urls', namespace='meetup_group')),
]

if settings.DEFAULT_FILE_STORAGE == 'django.core.files.storage.FileSystemStorage':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
