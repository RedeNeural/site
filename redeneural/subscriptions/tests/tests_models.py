from model_mommy import mommy

from django.test import TestCase

from redeneural.subscriptions.models import Subscription


class SubscriptionTestCase(TestCase):

    def setUp(self):
        self.obj = Subscription(event=mommy.make('event.Event'), name='name', email='email')
        self.obj.save()

        self.field_event = Subscription._meta.get_field('event')
        self.field_name = Subscription._meta.get_field('name')
        self.field_email = Subscription._meta.get_field('email')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.name)

    def test_event_cant_be_blank(self):
        self.assertFalse(self.field_event.blank)

    def test_event_cant_be_null(self):
        self.assertFalse(self.field_event.null)

    def test_name_cant_be_blank(self):
        self.assertFalse(self.field_name.blank)

    def test_name_cant_be_null(self):
        self.assertFalse(self.field_name.null)

    def test_email_cant_be_blank(self):
        self.assertFalse(self.field_email.blank)

    def test_email_cant_be_null(self):
        self.assertFalse(self.field_email.null)
