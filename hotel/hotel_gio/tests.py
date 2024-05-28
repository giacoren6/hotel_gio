from django.test import TestCase
from django.urls import reverse

class RoomsTestCase(TestCase):
    def test_rooms_view(self):
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms.html')
