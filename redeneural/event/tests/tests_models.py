from model_mommy import mommy

from datetime import datetime

from django.test import TestCase

from redeneural.event.models import Event


class EventModelTestCase(TestCase):

    def setUp(self):
        self.obj = Event(meetup_group=mommy.make('meetup_group.MeetupGroup'), name='Event', slug='event',
                         long_description='long_description', start_date=datetime.now().date(),
                         end_date=datetime.now().date())
        self.obj.save()

        self.field_meetup_group = Event._meta.get_field('meetup_group')
        self.field_name = Event._meta.get_field('name')
        self.field_slug = Event._meta.get_field('slug')
        self.field_short_description = Event._meta.get_field('short_description')
        self.field_long_description = Event._meta.get_field('long_description')
        self.field_start_date = Event._meta.get_field('start_date')
        self.field_end_date = Event._meta.get_field('end_date')
        self.field_start_time = Event._meta.get_field('start_time')
        self.field_end_time = Event._meta.get_field('end_time')
        self.field_location = Event._meta.get_field('location')
        self.field_image = Event._meta.get_field('image')
        self.field_banner = Event._meta.get_field('banner')
        self.field_limit_participants = Event._meta.get_field('limit_participants')
        self.field_open_subscriptions_on = Event._meta.get_field('open_subscriptions_on')
        self.field_close_subscriptions_on = Event._meta.get_field('close_subscriptions_on')
        self.field_is_active = Event._meta.get_field('is_active')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.name)

    def test_meetup_group_cant_be_blank(self):
        self.assertFalse(self.field_meetup_group.blank)

    def test_meetup_group_cant_be_null(self):
        self.assertFalse(self.field_meetup_group.null)

    def test_name_cant_be_blank(self):
        self.assertFalse(self.field_name.blank)

    def test_name_cant_be_null(self):
        self.assertFalse(self.field_name.null)

    def test_slug_cant_be_blank(self):
        self.assertFalse(self.field_slug.blank)

    def test_slug_cant_be_null(self):
        self.assertFalse(self.field_slug.null)

    def test_short_description_cant_be_blank(self):
        self.assertTrue(self.field_short_description.blank)

    def test_short_description_cant_be_null(self):
        self.assertTrue(self.field_short_description.null)

    def test_long_description_cant_be_blank(self):
        self.assertFalse(self.field_long_description.blank)

    def test_long_description_cant_be_null(self):
        self.assertFalse(self.field_long_description.null)

    def test_start_date_cant_be_blank(self):
        self.assertFalse(self.field_start_date.blank)

    def test_start_date_cant_be_null(self):
        self.assertFalse(self.field_start_date.null)

    def test_end_date_cant_be_blank(self):
        self.assertFalse(self.field_end_date.blank)

    def test_end_date_cant_be_null(self):
        self.assertFalse(self.field_end_date.null)

    def test_start_time_cant_be_blank(self):
        self.assertTrue(self.field_start_time.blank)

    def test_start_time_cant_be_null(self):
        self.assertTrue(self.field_start_time.null)

    def test_end_time_cant_be_blank(self):
        self.assertTrue(self.field_end_time.blank)

    def test_end_time_cant_be_null(self):
        self.assertTrue(self.field_end_time.null)

    def test_location_cant_be_blank(self):
        self.assertFalse(self.field_location.blank)

    def test_location_cant_be_null(self):
        self.assertFalse(self.field_location.null)

    def test_image_cant_be_blank(self):
        self.assertTrue(self.field_image.blank)

    def test_image_cant_be_null(self):
        self.assertTrue(self.field_image.null)

    def test_banner_cant_be_blank(self):
        self.assertTrue(self.field_banner.blank)

    def test_banner_cant_be_null(self):
        self.assertTrue(self.field_banner.null)

    def test_limit_participants_cant_be_blank(self):
        self.assertFalse(self.field_limit_participants.blank)

    def test_limit_participants_cant_be_null(self):
        self.assertFalse(self.field_limit_participants.null)

    def test_open_subscriptions_on_cant_be_blank(self):
        self.assertFalse(self.field_open_subscriptions_on.blank)

    def test_open_subscriptions_on_cant_be_null(self):
        self.assertFalse(self.field_open_subscriptions_on.null)

    def test_close_subscriptions_on_cant_be_blank(self):
        self.assertFalse(self.field_close_subscriptions_on.blank)

    def test_close_subscriptions_on_cant_be_null(self):
        self.assertFalse(self.field_close_subscriptions_on.null)

    def test_is_active_cant_be_blank(self):
        self.assertFalse(self.field_is_active.blank)

    def test_is_active_cant_be_null(self):
        self.assertFalse(self.field_is_active.null)
