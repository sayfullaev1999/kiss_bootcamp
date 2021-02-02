from django.test import TestCase
from django.urls import reverse

from ..models import Course
from account.models import User
from account.models import Mentor


class CourseViewTest(TestCase):
    def setUp(self) -> None:
        self.course_create_url = reverse('course_create_url')
        self.course_update_url = reverse('course_update_url', kwargs={'slug': 'some-course1'})
        self.course_delete_url = reverse('course_delete_url', kwargs={'slug': 'some-course1'})
        self.user1 = User.objects.create(
            username='some_user',
            first_name='First name',
            last_name='Last name',
            email='user1@example.com',
        )
        self.user1.set_password('TestPass123')
        self.user1.save()
        self.mentor1 = Mentor.objects.create(
            user=self.user1,
            info='Best Mentor',
            position='Backend Python Junior Developer'
        )
        self.user2 = User.objects.create(
            username='some_user2',
            first_name='First name2',
            last_name='Last name2',
            email='user2@example.com',
        )
        self.user2.set_password('TestPass123')
        self.user2.save()
        self.mentor2 = Mentor.objects.create(
            user=self.user2,
            info='Best Mentor2',
            position='Backend Python Junior Developer2'
        )
        self.course = Course.objects.create(
            name='Some course1',
            info='Some info1',
            image='some_image1.jpg',
        )
        self.course.mentor.add(self.mentor1)
        self.course.save()

    def test_course_create_GET(self):
        response = self.client.get(self.course_create_url)
        self.assertEquals(response.status_code, 302)

        login = self.client.login(username='some_user', password='TestPass123')
        self.assertTrue(login)

        self.client.force_login(self.user1)
        response = self.client.get(self.course_create_url)
        self.assertEquals(response.status_code, 200)

    def test_course_create_POST(self):
        response = self.client.post(self.course_create_url)
        self.assertEquals(response.status_code, 302)

        login = self.client.login(username='some_user', password='TestPass123')
        self.assertTrue(login)

        self.client.force_login(self.user1)
        response = self.client.post(
            self.course_create_url, {
                'name': 'Some course3',
                'info': 'Some info3',
                'image': 'some_course3.jpg',
                'mentor': self.mentor1
            }
        )
        self.assertEquals(response.status_code, 200)

    def test_course_update_GET(self):
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 302)

        self.client.force_login(self.user2)
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 403)

        self.client.force_login(self.user1)
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 200)

    def test_course_delete_GET(self):
        response = self.client.get(self.course_delete_url)
        self.assertEquals(response.status_code, 302)

        self.client.force_login(self.user2)
        response = self.client.get(self.course_delete_url)
        self.assertEquals(response.status_code, 403)

        self.client.force_login(self.user1)
        response = self.client.get(self.course_delete_url)
        self.assertEquals(response.status_code, 200)

    def test_course_delete_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.course_delete_url)
        self.assertEquals(response.status_code, 302)
