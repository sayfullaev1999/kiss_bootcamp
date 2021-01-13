from django.shortcuts import render
from django.views.generic import View
from general.generators import gen_paginator

from news.models import News
from news.forms import NewsForm
from general.mixins import ObjectDetailMixins, ObjectCreateMixins, ObjectUpdateMixins, ObjectDeleteMixins


def news_list(request):
    news = News.objects.all()
    context = gen_paginator(request, news, 4)
    return render(request, template_name='news/news_list.html', context=context)


class NewsDetail(ObjectDetailMixins, View):
    model = News
    template = 'news/news_detail.html'


class NewsCreate(ObjectCreateMixins, View):
    model = News
    model_form = NewsForm
    template = 'news/news_create.html'


class NewsUpdate(ObjectUpdateMixins, View):
    model = News
    model_form = NewsForm
    template = 'news/news_update.html'


class NewsDelete(ObjectDeleteMixins, View):
    model = News
    template = 'news/news_delete.html'
    redirect_url = 'news_list_url'