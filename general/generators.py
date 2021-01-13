from time import time

from django.core.paginator import Paginator
from django.utils.text import slugify


def gen_paginator(request, objects, per_page):
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    previous_url, next_url = ('', '')
    if page.has_previous():
        previous_url = f'?page={page.next_page_number()}'
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
    }
    return context


def gen_slug(string):
    new_slug = slugify(string, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
