from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from posts.models import Post


class Comment(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    text = models.TextField()
