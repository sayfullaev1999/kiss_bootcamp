from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import resolve

from ..views import CourseList
from ..views import CourseDetail
from ..views import CourseCreate
from ..views import CourseUpdate
from ..views import CourseDelete


class UrlTest(SimpleTestCase):
	def test_course_list_url(self):
		url = reverse('course_list_url')
		self.assertEquals(resolve(url).func.view_class, CourseList)

	def test_course_detail_url(self):
		url = reverse('course_detail_url', kwargs={'slug': 'some-course'})
		self.assertEquals(resolve(url).func.view_class, CourseDetail)

	def test_course_create_url(self):
		url = reverse('course_create_url')
		self.assertEquals(resolve(url).func.view_class, CourseCreate)

	def test_course_update_url(self):
		url = reverse('course_update_url', kwargs={'slug': 'some-course'})
		self.assertEquals(resolve(url).func.view_class, CourseUpdate)

	def test_course_delete_url(self):
		url = reverse('course_delete_url', kwargs={'slug': 'some-course'})
		self.assertEquals(resolve(url).func.view_class, CourseDelete)