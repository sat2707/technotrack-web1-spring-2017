# coding: utf-8
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404, resolve_url, reverse, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .models import Blog, Post
from likes.models import Like
from django import forms


class SortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('title', u'Заголовок'),
            ('rate', u'Рейтинг'),
            ('description', u'Описание'),
        ),
        required=False
    )
    search = forms.CharField(required=False)


class UpdateBlog(UpdateView):

    template_name = 'posts/editblog.html'
    model = Blog
    fields = ('title', 'description', 'categories')

    def get_success_url(self):
        return resolve_url('posts:oneblog', pk=self.object.id)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class UpdatePost(UpdateView):

    template_name = 'posts/editpost.html'
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('posts:onepost', pk=self.object.id)

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreateBlog(CreateView):

    template_name = 'posts/addblog.html'
    model = Blog
    fields = ('title', 'description', 'categories')
    success_url = '/blogs/'

    def get_success_url(self):
        return reverse('posts:oneblog', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class BlogsList(ListView):

    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            if self.sortform.cleaned_data['sort']:
                qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/post.html'


class PostCommentsView(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/commentsdiv.html'


class PostLikeView(View):

    post_object = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostLikeView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        like = self.post_object.likes.filter(author=self.request.user).first()
        if like is None:
            like = Like()
            like.author = self.request.user
            like.post = self.post_object
            like.save()
        else:
            like.delete()
        return HttpResponse(Like.objects.filter(post=self.post_object).count())
