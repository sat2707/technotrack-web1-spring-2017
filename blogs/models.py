from django.db import models
from django.conf import settings

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    title = models.CharField(max_length=255)
    text = models.TextField()
#    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title', )

    def __str__(self):
            return ' Блог : {title} '.format(title=self.title)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog', related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField()
#    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-created_at', )

    def __str__(self):
        return ' Пост #{id} - {title}'.format(id=self.id, title=self.title)

