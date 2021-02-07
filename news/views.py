from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.urls import reverse

from .models import News
from .models import Subscriber
from .forms import NewsForm
from .forms import SubscriberForm
from .utils import is_valid_status, is_valid_uuid4


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


class Subscribe(View):
    def get(self, request):
        raise Http404()

    def post(self, request):
        bound_form = SubscriberForm(request.POST)

        if bound_form.is_valid():
            subscriber = bound_form.save()
            email = subscriber.email
            uuid = subscriber.conf_uuid
            link = request.build_absolute_uri() + f'confirm/active/{uuid}'
            send_mail(
                subject='Subscribing Confirmation',
                from_email=settings.DEFAULT_FROM_EMAIL,
                message='',
                recipient_list=[email],
                html_message=f'Thank you for signing up!\nPlease complete the subscription process by clicking the <a href="{link}">link here</a>'
            )
        return redirect(reverse('home_url'))


class Confirm(View):
    def get(self, request, status, uuid):
        if not (is_valid_status(status) and is_valid_uuid4(uuid)):
            raise Http404()
        subscriber = get_object_or_404(Subscriber, conf_uuid=uuid)
        if status == 'active':
            subscriber.confirmed = True
        else:
            subscriber.confirmed = False
        subscriber.save()
        return redirect(reverse('home_url'))

    def post(self, request, status, uuid):
        raise Http404()
