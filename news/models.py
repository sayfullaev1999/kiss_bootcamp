from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from general.generators import gen_slug


class News(models.Model):
    """
    The News model
    The is_active field are optional (default=True). Other fields are required
    """
    title = models.CharField(_('title'), max_length=30)
    image = models.ImageField(_('image'))
    body = models.TextField(_('body'))
    slug = models.SlugField(_('URL'), max_length=255, unique=True, help_text=_('Human-readable URLs'))
    date_pub = models.DateTimeField(_('date published'), auto_now_add=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this news should be treated as active.'
            'Unselect this instead of deleting news.'
        )
    )

    def get_absolute_url(self):
        """
        Telling Django how to compute the canonical URL to get detail about the News object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        """
        Telling Django how to compute the canonical URL to get update about the News object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('news_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """
        Telling Django how to compute the canonical URL to get delete about the News object.
        For callers, this method should return a string that can be used to refer to the object over HTTP.
        """
        return reverse('news_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Generating a slug for the object before saving
        """
        if not self.id:
            # We use title as a slug
            self.slug = gen_slug(self.title)
        # Calling the parent method
        super(News, self).save(*args, **kwargs)

    class Meta:
        """
        Sort news in descending order of publication date
        """
        ordering = ['-date_pub']
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __str__(self):
        """
        Return the news title.
        """
        return self.title


