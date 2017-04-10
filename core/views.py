from django.views.generic import TemplateView
from posts.models import Blog, Post
from comments.models import Comment


class MainPage(TemplateView):

    template_name = 'core/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['blogs_count'] = Blog.objects.count()
        context['posts_count'] = Post.objects.count()
        context['comments_count'] = Comment.objects.count()
        return context
