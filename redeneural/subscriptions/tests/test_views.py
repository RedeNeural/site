from model_mommy import mommy

from django.urls import reverse_lazy
from django.test import TestCase

from redeneural.subscriptions.models import Subscription


class FormTestGetTestCase(TestCase):

    def setUp(self):
        self.event = mommy.make('event.Event', is_active=True)
        self.response = self.client.get(reverse_lazy('subscriptions:form', args=[self.event.slug]))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/form.html')


class FormTestGetNotFoundTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse_lazy('subscriptions:form', args=['not-found']))

    def test_get(self):
        self.assertEqual(404, self.response.status_code)


class FormTestPostValidTestCase(TestCase):

    def setUp(self):
        self.event = mommy.make('event.Event', is_active=True)
        data = {
            'name': 'test',
            'email': 'test@test.com',
        }
        self.response = self.client.post(reverse_lazy('subscriptions:form', args=[self.event.slug]), data=data)

    def test_subscription_exist(self):
        self.assertTrue(Subscription.objects.exists())


class FormTestPostInvalidTestCase(TestCase):

    def setUp(self):
        self.event = mommy.make('event.Event', is_active=True)
        data = {
            'name': 'test',
            'email': 'test@test.com',
        }
        mommy.make(Subscription, event=self.event, name=data['name'], email=data['email'])

        self.response = self.client.post(reverse_lazy('subscriptions:form', args=[self.event.slug]), data=data)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_form_invalid(self):
        self.assertEqual(self.response.context['form'].errors['__all__'],
                         ['Sua inscrição já está feita para esse evento.'])
