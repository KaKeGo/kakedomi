from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_category_absolute_url(self):
        return reverse('blogs:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blogs/thumbnails/')
    category = models.ManyToManyField('Category', related_name='blog_category')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_likes', null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return f'{self.title} / {self.author.username}'

    def get_blogs_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '-' + self.author.username)
        super(Blog, self).save(*args, **kwargs)
