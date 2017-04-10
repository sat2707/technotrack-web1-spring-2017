from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Like(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('posts.Post')

    class Meta:
        unique_together = ('author', 'post')
