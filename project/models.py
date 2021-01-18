from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from account.models import User


class Project(models.Model):
    """
    The Project model which is related to the User model ManyToMany.
    All fields are required
    """
    name = models.CharField(_('name'), max_length=150)
    info = models.TextField(_('information'))
    image = models.ImageField(_('image'))
    users = models.ManyToManyField(User, related_name='projects', verbose_name='user')
    slug = models.SlugField(
        _('URL'),
        max_length=255,
        unique=True,
        help_text=_('Human-readable URLs'),
        error_messages={
            'unique': _('A course with that slug already exists.'),
        }
    )
    site = models.URLField(_('web site'), max_length=150, blank=True, help_text=_('A web site of project'))

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the Project object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('project_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Generating a slug for the object before saving
        """
        if not self.id:
            # We use name as a slug
            self.slug = self.name.lower()
        # Calling the parent method
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __str__(self):
        """
        Return the project name .
        """
        return self.name
