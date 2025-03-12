from django.contrib import admin

from .models import Post, Tag, PostImages


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'outline', 'body', 'tags']
    list_display = ['title', 'created_at']
    list_display_links = ['title',]
    list_filter = ['created_at',]


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)
