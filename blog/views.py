from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Tag, Post, PostImages


def index(request):
    recent_posts = Post.objects.all()[:4]
    return render(request, 'home.html', {'posts': recent_posts})


def blog_view(request):
    tags = Tag.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog.html',
                  {
                    'tags': tags,
                    'posts': posts
                   }
                  )


def post_view(request, post_pk):
    return HttpResponse(f'Post: {post_pk}')


def contacts_view(request):
    return HttpResponse("Contacts page")
