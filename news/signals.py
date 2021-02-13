from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from django.conf import settings

from .models import News
from .tasks import send_news
from .models import Subscriber


@receiver(post_save, sender=News)
def send_news_to_email(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscriber.objects.filter(confirmed=True)
        subject = 'Great News'
        message = ''
        current_site = Site.objects.get_current()
        link = f'{settings.PROTOCOL}://{current_site.domain}{instance.get_absolute_url()}'
        html_message = f'We are glad to inform you about new news {instance.title} ' \
                       f'click on <a href="{link}">the link</a> to find out more'
        emails = []
        for subscriber in subscribers:
            emails.append(subscriber.email)
        if emails:
            send_news.delay(subject, message, emails, html_message)
