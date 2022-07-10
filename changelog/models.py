from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class ChangeLog(models.Model):
    title = models.CharField(max_length=40, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Change log`s'
        verbose_name = 'Change Log'
        
    def __str__(self):
        return f'{self.title}'
    
    def get_changelog_absolute_url(self):
        return reverse('changelog:details', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title) + str(self.author) + str(self.author.id))
        super(ChangeLog, self).save(*args, **kwargs)
