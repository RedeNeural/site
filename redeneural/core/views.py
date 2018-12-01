from django.shortcuts import render

from redeneural.banner.models import Banner
from redeneural.event.models import Event


def home(request):
    context = {
        'banners': Banner.objects.all(),
        'evento_destaque': Event.objects.get_next_event(),
        'proximos_eventos': Event.objects.all()
    }
    return render(request, 'core/index.html', context)
