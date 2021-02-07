from django.test import TestCase
from django.urls import reverse

from ..models import Subscriber


class ViewTest(TestCase):
    def setUp(self) -> None:
        self.subscriber = Subscriber.objects.create(
            email='some_email@example.com'
        )
        self.subscribe_url = reverse('subscribe_url')
        self.confirm_url = reverse('confirm_url', kwargs={'status': 'active', 'uuid': str(self.subscriber.conf_uuid)})

    def test_subscribe_GET(self):
        response = self.client.get(self.subscribe_url)
        self.assertEquals(response.status_code, 404)

    def test_subscribe_POST(self):
        response = self.client.post(self.subscribe_url, data={'email': 'some_email@example.com'})
        self.assertEquals(response.status_code, 302)

    def test_confirm_GET(self):
        response = self.client.get(reverse('confirm_url', kwargs={'status': 'active', 'uuid': 'some-uuid'}))
        self.assertEquals(response.status_code, 404)
        response = self.client.get(
            reverse('confirm_url', kwargs={'status': 'some-status', 'uuid': str(self.subscriber.conf_uuid)}))
        self.assertEquals(response.status_code, 404)

        response = self.client.get(self.confirm_url)
        self.assertEquals(response.status_code, 302)

    def test_confirm_POST(self):
        response = self.client.post(self.confirm_url)
        self.assertEquals(response.status_code, 404)
