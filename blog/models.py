from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


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


class PostImages(models.Model):
    img_name = models.CharField(max_length=150, blank=False, null=False)
    post = models.ForeignKey(Post, related_name='images',
                             on_delete=models.CASCADE)
    image_path = models.ImageField(blank=False, null=False,
                                   upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.img_name
