from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Поля пользователь сайта """

    email = models.EmailField(
        max_length=60,
        unique=True,
        verbose_name='Адресс электронной почты'
    )
    image = models.ImageField(
        verbose_name='Фото профиля',
        blank=True,
    )
    info = models.TextField(
        verbose_name='Информация'
    )
    is_mentor = models.BooleanField(
        default=False,
        verbose_name='Статус учителя'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Sponsor(models.Model):
    """ Модель Спонсоров """
    organization = models.CharField(
        max_length=30,
        verbose_name='Имя Организации',
    )
    body = models.TextField(
        verbose_name='Информация',
    )
    logo = models.ImageField(
        verbose_name='Логотип',
    )
    site = models.CharField(
        max_length=30,
        verbose_name='Веб сайт',
        blank=True
    )

    class Meta:
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'

    def __str__(self):
        return self.organization
