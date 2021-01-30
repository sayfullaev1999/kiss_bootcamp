from django.test import TestCase
from django.urls import reverse

from ..models import User
from ..models import Mentor
from ..models import Sponsor


class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='some_user',
            first_name='First name',
            last_name='Last name',
            email='user1@example.com',
        )

    def test_object_name_is_username(self):
        self.assertEquals(str(self.user.username), 'some_user')


class MentorModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='some_user',
            first_name='First name',
            last_name='Last name',
            email='user1@example.com',
        )
        self.mentor = Mentor.objects.create(
            user=User.objects.last(),
            info='Best Mentor',
            position='Backend Python Junior Developer'
        )

    def test_object_name_is_username(self):
        self.assertEquals(str(self.mentor.user.username), 'some_user')

    def test_slug_is_username(self):
        self.assertEquals(self.mentor.slug, 'some_user')

    def test_mentor_get_absolute_url(self):
        url = reverse('mentor_detail_url', kwargs={'slug': self.mentor.user.username})
        self.assertEquals(self.mentor.get_absolute_url(), url)


class SponsorModelTest(TestCase):
    def setUp(self) -> None:
        self.sponsor = Sponsor.objects.create(
            name='UB TUIT',
            body='Urgench Branch of Tashkent university of Information Technologies named After Muhammad al - Khwarizmi',
            site='https://ubtuit.uz/',
        )

    def test_slug_is_name_lower_case(self):
        self.assertEquals(self.sponsor.slug, 'ub-tuit')

    def test_sponsor_get_absolute_url(self):
        url = reverse('sponsor_detail_url', kwargs={'slug': self.sponsor.slug})
        self.assertEquals(self.sponsor.get_absolute_url(), url)
