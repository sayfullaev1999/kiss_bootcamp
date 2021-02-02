from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import resolve

from ..views import ProjectList
from ..views import ProjectDetail


class UrlTest(SimpleTestCase):
    def test_project_list_url(self):
        url = reverse('project_list_url')
        self.assertEquals(resolve(url).func.view_class, ProjectList)

    def test_project_detail_url(self):
        url = reverse('project_detail_url', kwargs={'slug': 'some-title'})
        self.assertEquals(resolve(url).func.view_class, ProjectDetail)