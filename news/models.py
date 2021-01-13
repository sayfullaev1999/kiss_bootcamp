from django.db import models
from django.urls import reverse

from general.generators import gen_slug


class News(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Заголовок',
    )
    image = models.ImageField(
        verbose_name='Фото'
    )
    body = models.TextField(
        verbose_name='Тело'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )
    date_pub = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('news_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('news_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    info = models.TextField(
        verbose_name='Информация'
    )
    image = models.ImageField(
        verbose_name='Фото',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name