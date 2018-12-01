from django.test import TestCase
from django.urls import reverse_lazy


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse_lazy('core:home'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_context(self):
        self.assertIn('banners', self.response.context.keys())
