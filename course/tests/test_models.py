from django.test import TestCase
from django.urls import reverse


from ..models import Course
from ..models import ContactUs
from account.models import Mentor
from account.models import User


class CourseModelTest(TestCase):
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
		self.course = Course.objects.create(name='Some course', info='Some text', image='some_image.jpg')
		self.course.mentor.add(self.mentor)
		self.course.save()


	def test_course_is_assigned_slug_on_creation(self):
		self.assertEquals(self.course.slug, 'some-course')

	def test_get_absolute_url(self):
		url = reverse('course_detail_url', kwargs={'slug': 'some-course'})
		self.assertEquals(self.course.get_absolute_url(), url)

	def test_get_update_url(self):
		url = reverse('course_update_url', kwargs={'slug': 'some-course'})
		self.assertEquals(self.course.get_update_url(), url)

	def test_get_delete_url(self):
		url = reverse('course_delete_url', kwargs={'slug': 'some-course'})
		self.assertEquals(self.course.get_delete_url(), url)

	def test_object_name_is_course_name(self):
		self.assertEquals(str(self.course), 'Some course')


class ContactUsModelTest(TestCase):
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
		self.course = Course.objects.create(name='Some course', info='Some text', image='some_image.jpg')
		self.course.mentor.add(self.mentor)
		self.course.save()
		self.contact_us = ContactUs(full_name='Some user', phone_number='+11111111', course=self.course)

	def test_object_name_is_full_name_concate_phone_number(self):
		self.assertEquals(str(self.contact_us), 'Some user +11111111')

	