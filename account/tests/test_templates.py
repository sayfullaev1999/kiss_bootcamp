from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from ..models import User
from ..models import Mentor
from ..models import Sponsor


class MentorTemplatesTest(TestCase):
    def setUp(self) -> None:
        self.mentor_list_url = reverse('mentor_list_url')
        self.mentor_detail_url = reverse('mentor_detail_url', kwargs={'slug': 'some_user'})
        self.mentor_list_template = 'account/mentor_list.html'
        self.mentor_detail_template = 'account/mentor_detail.html'
        self.user = User.objects.create(
            username='some_user',
            first_name='First name',
            last_name='Last name',
            email='user@example.com',
        )
        self.mentor = Mentor.objects.create(
            user=User.objects.get(username='some_user'),
            image='some_mentor.jpg',
            info='Best Mentor',
            position='Backend Python Junior Developer'
        )

    def test_mentor_list_page(self):
        response = self.client.get(self.mentor_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.mentor_list_template)
        self.assertContains(response, 'First name')

    def test_mentor_detail_page(self):
        response = self.client.get(self.mentor_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.mentor_detail_template)
        self.assertContains(response, 'First name')


class SponsorTemplatesTest(TestCase):
    def setUp(self) -> None:
        self.sponsor_list_url = reverse('sponsor_list_url')
        self.sponsor_list_template = 'account/sponsor_list.html'
        self.sponsor_detail_url = reverse('sponsor_detail_url', kwargs={'slug': slugify('some-sponsor-3')})
        self.sponsor_detail_template = 'account/sponsor_detail.html'
        number_of_sponsors = 10
        for num_sponsor in range(number_of_sponsors):
            Sponsor.objects.create(
                name=f'Some sponsor {num_sponsor}',
                body=f'Some body {num_sponsor}',
                logo=f'some_logo_{num_sponsor}.jpg',
            )

    def test_sponsor_list_page(self):
        response = self.client.get(self.sponsor_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.sponsor_list_template)
        self.assertContains(response, 'Some sponsor 1')
        self.assertContains(response, 'Some sponsor 9')

    def test_sponsor_detail_page(self):
        response = self.client.get(self.sponsor_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.sponsor_detail_template)
        self.assertContains(response, 'Some sponsor 3')


class UserTemplateTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.register_template = 'registration/register.html'
        self.login_url = reverse('login')
        self.login_template = 'registration/login.html'

    def test_register_page(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.register_template)

    def test_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.login_template)
