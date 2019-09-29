from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    todo_id = models.IntegerField()
    name = models.CharField(_("Name"), max_length= 255)
    done = models.BooleanField(_("Done"), default=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Todos")
        verbose_name_plural = _("Todos")
    def __unicode__(self):
        return smart_unicode(self.name)
