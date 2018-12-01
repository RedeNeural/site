from django import forms

from redeneural.subscriptions import models


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = models.Subscription
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)

        super(SubscriptionForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data.copy()

        email = data.get('email')

        if email and self.event.subscriptions.filter(email=email).exists():
            raise forms.ValidationError('Sua inscrição já está feita para esse evento.')

        return data
