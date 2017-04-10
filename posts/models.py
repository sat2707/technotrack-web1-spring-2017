from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()

    def __unicode__(self):
        return self.title


class Post(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    text = models.TextField()
    blog = models.ForeignKey(Blog, models.DO_NOTHING)

    def __unicode__(self):
        return self.title