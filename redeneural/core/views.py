from django.shortcuts import render

from redeneural.banner.models import Banner


def home(request):
    context = {
        'banners': Banner.objects.all()
    }

    return render(request, 'core/index.html', context)
