from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Tag, Post, PostImages


def index(request):
    return render(request, 'home.html')


def blog_view(request):
    return HttpResponse('Blog page')


def post_view(request, post_pk):
    return HttpResponse(f'Post: {post_pk}')


def contacts_view(request):
    return HttpResponse("Contacts page")
