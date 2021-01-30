from django.test import TestCase
from django.urls import reverse

from ..models import User


class ViewTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_POST_add_new_user(self):
        response = self.client.post(
            self.register_url, {
                'username': 'some_user',
                'first_name': 'First name',
                'last_name': 'Last name',
                'email': 'user@example.com',
                'password1': 'TestPasswordSomeUser123',
                'password2': 'TestPasswordSomeUser123'
            }
        )
        self.assertEquals(response.status_code, 302)

    def test_register_POST_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.all().count(), 0)
