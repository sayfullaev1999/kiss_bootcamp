from time import time
from django.utils.text import slugify


def gen_slug(string):
    new_slug = slugify(string, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
