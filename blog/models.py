from django.db import models
from django.template.defaultfilters import slugify


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
    tags = models.ForeignKey(Tag, related_name='posts',
                             null=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class PostImages(models.Model):
    img_name = models.CharField(max_length=150, blank=False, null=False)
    post = models.ForeignKey(Post, related_name='images',
                             on_delete=models.CASCADE)
    image_path = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.img_name
