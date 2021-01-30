from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    The image fields are optional. Other fields are required.
    """

    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), max_length=60, unique=True)
    image = models.ImageField(_('photo'), blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        """
        Return the username of user
        """
        return self.get_username()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Mentor(models.Model):
    """
    The Mentor model which is related to the User model OneToOne.
    All fields are required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')
    image = models.ImageField(_('photo'))
    info = models.TextField(_('information'))
    position = models.CharField(
        _('position'),
        max_length=150,
        help_text=_(
            'Example: Junior Software Developer, Web Developer, Front End Developer... '
        )
    )
    slug = models.SlugField(
        _('URL'),
        max_length=150,
        unique=True,
        help_text=_('Human-readable URLs'),
        error_messages={
            'unique': _("A mentor with that username already exists."),
        },
    )

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the Mentor object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('mentor_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        """
        Return the mentor username.
        """
        return self.user.get_username()

    def save(self, *args, **kwargs):
        """
            Generating a slug for the object before saving
        """
        if not self.pk:
            # We use username as a slug
            self.slug = self.user.username
        # Calling the parent method
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('mentor')
        verbose_name_plural = _('mentors')


class Sponsor(models.Model):
    """
    The Sponsor model
    Site field is optional. Other fields are required
    """
    name = models.CharField(
        _('name'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A sponsor that name already exists."),
        },
    )
    body = models.TextField(_('information'))
    logo = models.ImageField(_('logo'))
    site = models.URLField(_('web site'), max_length=150, blank=True, help_text=_('A web site of sponsor'))
    slug = models.SlugField(_('URL'), unique=True, help_text=_('Human-readable URLs'))

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the Sponsor object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('sponsor_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Generating a slug for the object before saving
        """
        if not self.pk:
            # We use name as a slug
            self.slug = slugify(self.name)
        # Calling the parent method
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'

    def __str__(self):
        """
        Return the Sponsor name.
        """
        return self.name
