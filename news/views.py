from django.views.generic import View, DetailView
from django.views.generic.list import ListView

from news.mixins import NewsUpdateMixin, NewsCreateMixin, NewsDeleteMixin
from news.models import News
from news.forms import NewsForm


class NewsList(ListView):
    queryset = News.objects.all()
    paginate_by = 1
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsCreate(NewsCreateMixin, View):
    model = News
    form_class = NewsForm
    template_name = 'news/news_create.html'


class NewsUpdate(NewsUpdateMixin, View):
    model = News
    form_class = NewsForm
    template_name = 'news/news_update.html'


class NewsDelete(NewsDeleteMixin, View):
    model = News
    template_name = 'news/news_delete.html'
    success_url = 'news_list_url'
