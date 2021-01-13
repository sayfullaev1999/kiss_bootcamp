from django.db import models
from django.urls import reverse

from account.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Имя курса',
    )
    info = models.TextField(
        verbose_name='Информация о курсе',
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='URL'
    )
    image = models.ImageField(
        verbose_name='Фото'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Учитель',
        on_delete=models.CASCADE,
        related_name='course'
    )

    def get_absolute_url(self):
        return reverse('course_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('course_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('course_delete_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    full_name = models.CharField(
        max_length=50,
        verbose_name='Полное имя',
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='Номер телефона',
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'{self.full_name}\n{self.phone_number}'