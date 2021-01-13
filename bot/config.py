import os
from enum import Enum
from django.conf import settings

if settings.DEBUG:
    TOKEN = os.getenv('LOCAL_TOKEN')
else:
    TOKEN = os.getenv('PRODUCTION_TOKEN')


class States(Enum):
    START = 0
    LESSONS = 1
    LESSON = 2
    HOME_CONTACT = 10
    SEND_CONTACT = 11
    SEND_NAME = 12
    TEACHER = 20
    SEND_NEWS = 30


DB_FILE = 'db.vdb'
