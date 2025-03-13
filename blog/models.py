from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    outline = models.CharField(max_length=255, default='')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-view', kwargs={'post_slug': self.slug})

    def get_body_as_html(self):
        return markdownify(self.body)

    class Meta:
        ordering = ['-created_at']
