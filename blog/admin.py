from django.contrib import admin

from .models import Post, Tag, PostImages


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostImages)
