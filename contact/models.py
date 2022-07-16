from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Contact(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    postman = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Contact messages'
        verbose_name = 'Message'

    def __str__(self):
        return f'{self.title} / {self.postman.username}'

    def get_message_absolute_url(self):
        return reverse('contact:contact', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ContactMessage, self).save(*args, **kwargs)
