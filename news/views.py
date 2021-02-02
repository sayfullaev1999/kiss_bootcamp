from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import News
from .forms import NewsForm


class NewsList(ListView):
    queryset = News.objects.all()
    paginate_by = 1
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsCreate(PermissionRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_create.html'
    permission_required = ''


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_update.html'
    permission_required = ''


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list_url')
    permission_required = ''
