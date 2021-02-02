from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from account.models import Mentor


class Course(models.Model):
    """
    The Course model which is related to the Mentor model ManyToMany.
    All fields are required
    """
    name = models.CharField(
        _('name'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _('A course with that name already exists.'),
        }
    )
    info = models.TextField(_('information'))
    slug = models.SlugField(
        _('URL'),
        max_length=255,
        unique=True,
        help_text=_('Human-readable URLs'),
        error_messages={
            'unique': _('A course with that slug already exists.'),
        }
    )
    image = models.ImageField(_('image'))
    mentor = models.ManyToManyField(Mentor, related_name='courses', verbose_name='mentor')

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the Course object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('course_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """
        Telling Django how to compute the canonical URL to get update about the Course object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('course_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """
        Telling Django how to compute the canonical URL to get delete about the Course object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('course_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Generating a slug for the object before saving
        """
        if not self.id:
            # We use name as a slug
            self.slug = slugify(self.name.lower())
        # Calling the parent method
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        permissions = ''

    def __str__(self):
        """
        Return the course name.
        """
        return self.name


class ContactUs(models.Model):
    """
    The ContactUs model which is related to the Course model OneToOne.
    The chat_id field are optional. Other fields are required
    """
    chat_id = models.PositiveIntegerField(
        _('telegram user id'),
        blank=True,
        help_text=_('Leave the fields blank if you want to create an entry from the site')
    )
    full_name = models.CharField(_('full name'), max_length=150)

    phone_number = models.CharField(_('phone number'), max_length=13)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='contact_us',
        verbose_name='course'
    )
    check_box = models.BooleanField(
        _('viewed'),
        default=False,
        help_text=_(
            'The fields indicate whether the record has been viewed'
            'Check this box if the entry is verified'
        )
    )

    date = models.DateTimeField(_('date'), auto_now=True)

    class Meta:
        verbose_name = _('contact us')
        verbose_name_plural = _('contact us')

    def __str__(self):
        """
        Return the full_name plus the phone_number, with a space in between.
        """
        return f'{self.full_name} {self.phone_number}'
