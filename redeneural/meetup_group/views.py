from django.shortcuts import render

from redeneural.meetup_group.models import MeetupGroup


def index(request):
    context = {
        'groups': MeetupGroup.objects.all(),
    }
    return render(request, 'meetup_group/index.html', context)
