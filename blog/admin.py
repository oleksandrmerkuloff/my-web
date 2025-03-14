from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    fields = ['title', 'outline', 'body', 'tags']
    list_display = ['title', 'created_at']
    list_display_links = ['title',]
    list_filter = ['created_at',]
    search_fields = ['title',]

    class Meta:
        js = ("markdownx/js/markdownx.js",)
        css = {"all": ("markdownx/css/markdownx.css",)}


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
