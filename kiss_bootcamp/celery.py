import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kiss_bootcamp.settings')

app = Celery('kiss_bootcamp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
