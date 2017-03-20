from django.db import models
from django.conf import settings
from blogs.models import Post

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('blogs.Post', related_name='comments')
    title = models.CharField(max_length=255)
    text = models.TextField()
    #    rate = models.IntegerField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'Комментарий #{id} - {title}'.format(id=self.id, title=self.title)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at', )


