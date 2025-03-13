from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tag, Post


def index(request):
    recent_posts = Post.objects.all()[:4]
    return render(request, 'home.html', {'posts': recent_posts})


def blog_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__name=tag)
    elif 'searching_title' in request.GET:
        title = request.GET.get('searching_title')
        posts = Post.objects.filter(title__icontains=title)
    else:
        posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog.html',
                  {
                    'tags': tags,
                    'posts': posts
                   }
                  )


def post_view(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'single-post.html', {'post': post})


def contacts_view(request):
    return render(request, 'contacts_page.html')
