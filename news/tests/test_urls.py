from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import resolve

from ..views import NewsList
from ..views import NewsDetail
from ..views import NewsCreate
from ..views import NewsUpdate
from ..views import NewsDelete


class UrlTest(SimpleTestCase):
    def test_news_list_url(self):
        url = reverse('news_list_url')
        self.assertEquals(resolve(url).func.view_class, NewsList)

    def test_news_detail_url(self):
        url = reverse('news_detail_url', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(url).func.view_class, NewsDetail)

    def test_news_create_url(self):
        url = reverse('news_create_url')
        self.assertEquals(resolve(url).func.view_class, NewsCreate)

    def test_news_update_url(self):
        url = reverse('news_update_url', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(url).func.view_class, NewsUpdate)

    def test_news_delete_url(self):
        url = reverse('news_delete_url', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(url).func.view_class, NewsDelete)
