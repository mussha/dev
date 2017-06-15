from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.

class SearchWordTeacherRecord(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    word = models.CharField(max_length=512)
    subject = models.ForeignKey(to='variables.Subject_Expertise', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.word, self.created)
