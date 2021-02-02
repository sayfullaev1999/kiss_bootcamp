from django.test import TestCase
from django.urls import reverse

from ..models import News
from general.generators import gen_slug


class NewsModelTest(TestCase):
    def setUp(self) -> None:
        self.news = News.objects.create(
            title='some title',
            image='some_image.jpg',
            body='some text',
        )

    def test_object_name_is_news_title(self):
        self.assertEquals(str(self.news), 'some title')

    def test_slug_is_gen_slug_title(self):
        self.assertEquals(self.news.slug, gen_slug('some title'))

    def test_news_get_absolute_url(self):
        url = reverse('news_detail_url', kwargs={'slug': gen_slug('some title')})
        self.assertEquals(self.news.get_absolute_url(), url)

    def test_news_get_update_url(self):
        url = reverse('news_update_url', kwargs={'slug': gen_slug('some title')})
        self.assertEquals(self.news.get_update_url(), url)

    def test_news_get_delete_url(self):
        url = reverse('news_delete_url', kwargs={'slug': gen_slug('some title')})
        self.assertEquals(self.news.get_delete_url(), url)