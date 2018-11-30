from django.test import TestCase

from redeneural.meetup_group.models import MeetupGroup


class MeetupGroupTestCase(TestCase):

    def setUp(self):
        self.obj = MeetupGroup(name='Group', slug='group', description='description')
        self.obj.save()

        self.field_name = MeetupGroup._meta.get_field('name')
        self.field_slug = MeetupGroup._meta.get_field('slug')
        self.field_description = MeetupGroup._meta.get_field('description')
        self.field_image = MeetupGroup._meta.get_field('image')
        self.field_cover_image = MeetupGroup._meta.get_field('cover_image')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.name)

    # NAME
    def test_name(self):
        self.assertEqual(self.obj.name, 'Group')

    def test_name_cant_be_blank(self):
        self.assertFalse(self.field_name.blank)

    def test_name_cant_be_null(self):
        self.assertFalse(self.field_name.null)

    # SLUG
    def test_slug(self):
        self.assertEqual(self.obj.slug, 'group')

    def test_slug_cant_be_blank(self):
        self.assertFalse(self.field_slug.blank)

    def test_slug_cant_be_null(self):
        self.assertFalse(self.field_slug.null)

    # SLUG
    def test_description(self):
        self.assertEqual(self.obj.description, 'description')

    def test_description_cant_be_blank(self):
        self.assertFalse(self.field_description.blank)

    def test_description_cant_be_null(self):
        self.assertFalse(self.field_description.null)

    # IMAGE
    def test_image_cant_be_blank(self):
        self.assertTrue(self.field_image.blank)

    def test_image_cant_be_null(self):
        self.assertTrue(self.field_image.null)

    # COVER IMAGE
    def test_cover_image_cant_be_blank(self):
        self.assertTrue(self.field_cover_image.blank)

    def test_cover_image_cant_be_null(self):
        self.assertTrue(self.field_cover_image.null)
