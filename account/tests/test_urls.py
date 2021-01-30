from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import Register, MentorList, MentorDetail, SponsorList, SponsorDetail


class UrlTest(SimpleTestCase):
    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, Register)

    def test_mentor_list_url(self):
        url = reverse('mentor_list_url')
        self.assertEquals(resolve(url).func.view_class, MentorList)

    def test_mentor_detail_url(self):
        url = reverse('mentor_detail_url', kwargs={'slug': 'some-mentor'})
        self.assertEquals(resolve(url).func.view_class, MentorDetail)

    def test_sponsor_list_url(self):
        url = reverse('sponsor_list_url')
        self.assertEquals(resolve(url).func.view_class, SponsorList)

    def test_sponsor_detail_url(self):
        url = reverse('sponsor_detail_url', kwargs={'slug': 'some_sponsor'})
        self.assertEquals(resolve(url).func.view_class, SponsorDetail)