from django.test import TestCase

from redeneural.banner.models import Banner


class BannerModelTest(TestCase):

    def setUp(self):
        self.obj = Banner(image='Title')
        self.obj.save()

        self.field_image = Banner._meta.get_field('image')
        self.field_link = Banner._meta.get_field('link')

    def test_str(self):
        self.assertEqual(str(self.obj), str(self.obj.id))

    # IMAGE
    def test_image_cant_be_blank(self):
        self.assertFalse(self.field_image.blank)

    def test_image_cant_be_null(self):
        self.assertFalse(self.field_image.null)

    # SLUG
    def test_link_can_be_blank(self):
        self.assertTrue(self.field_link.blank)

    def test_link_cant_be_null(self):
        self.assertTrue(self.field_link.null)
