from django.db import models


class Lesson(models.Model):
    """ Поля Курс """

    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    info = models.TextField(
        verbose_name='Информация'
    )
    image = models.ImageField(
        verbose_name='Рисунок'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """ Поля Учитель """

    name = models.CharField(
        max_length=50,
        verbose_name='Фамилия и имя'
    )
    image = models.ImageField(
        verbose_name='Рисунок'
    )
    info = models.TextField(
        verbose_name='Информация'
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name='Электронная почта'
    )

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Contact(models.Model):
    """ Поля для обратной связи """

    chat_id = models.IntegerField(
        verbose_name='ID чата'
    )

    name = models.CharField(
        blank=False,
        max_length=50,
        verbose_name="Имя",
        null=False,
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона",
    )
    check_box = models.BooleanField(
        default=False,
        verbose_name='Просмотрен'
    )

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата"
    )
    lesson = models.OneToOneField(
        to=Lesson,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name


class Info(models.Model):
    """ Информация о нас """

    text = models.TextField(
        null=False,
        verbose_name='Информация'
    )

    class Meta:
        verbose_name = 'Информация о нас'
        verbose_name_plural = 'Информация о нас'


class UserBot(models.Model):
    chat_id = models.PositiveIntegerField(
        verbose_name='ID пользователя'
    )
    username = models.CharField(
        max_length=33,
        verbose_name='Уникальное имя пользователя'
    )
    language_bot = models.CharField(
        max_length=2,
        verbose_name='Язык интерфейса бота',
        default='UZ',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
