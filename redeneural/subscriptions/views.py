from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404


from redeneural.subscriptions import forms
from redeneural.subscriptions import models
from redeneural.event.models import Event


def form(request, event_slug):
    event = get_object_or_404(Event.objects.filter(is_active=True), slug=event_slug)
    form = forms.SubscriptionForm(event=event)

    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.SubscriptionForm(event=event, data=data)

        if form.is_valid():
            models.Subscription.objects.create(event=event,
                                               name=form.cleaned_data['name'],
                                               email=form.cleaned_data['email'])

            return redirect(reverse_lazy('core:home'))

    context = {
        'form': form
    }

    return render(request, 'subscriptions/form.html', context)
