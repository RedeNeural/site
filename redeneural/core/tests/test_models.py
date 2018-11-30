from django.test import TestCase

from redeneural.core.models import About


class AboutModelTestCase(TestCase):

    def setUp(self):
        self.obj = About(content='content')
        self.obj.save()

        self.field_content = About._meta.get_field('content')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.content)

    # content
    def test_content_cant_be_blank(self):
        self.assertFalse(self.field_content.blank)

    def test_content_cant_be_null(self):
        self.assertFalse(self.field_content.null)
