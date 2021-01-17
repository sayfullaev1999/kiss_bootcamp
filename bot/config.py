import os
from enum import Enum
from django.conf import settings

if settings.DEBUG:
    TOKEN = os.getenv('LOCAL_TOKEN')
else:
    TOKEN = os.getenv('PRODUCTION_TOKEN')


class States(Enum):
    START = 0
    COURSE = 10
    HOME_CONTACT = 20
    SEND_CONTACT = 11
    SEND_NAME = 30
    MENTOR = 40
    SEND_NEWS = 50


DB_FILE = 'db.vdb'
