from model_mommy import mommy
from django.test import TestCase
from django.urls import reverse_lazy


class IndexTest(TestCase):

    def setUp(self):
        mommy.make('meetup_group.MeetupGroup', name="Grupo Teste")
        self.response = self.client.get(reverse_lazy('meetup_group:home'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'meetup_group/index.html')
