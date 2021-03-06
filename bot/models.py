from django.db import models
from django.utils.translation import gettext_lazy as _


class UserBot(models.Model):
    """
    The UserBot model
    """
    chat_id = models.PositiveIntegerField(_('ID'), unique=True, help_text=_('telegram user id'))
    username = models.CharField(_('username'), max_length=33, blank=True, default='None')
    language_bot = models.CharField(_('language'), max_length=2, default='UZ')

    def __str__(self):
        """
        Return the username.
        """
        return self.username

    class Meta:
        verbose_name = _('telegram user')
        verbose_name_plural = _('telegram users')
