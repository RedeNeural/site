from django import forms

from redeneural.subscriptions import models


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = models.Subscription
        fields = ['name', 'email']
