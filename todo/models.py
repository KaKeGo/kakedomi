from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

# Create your models here.


class ToDo(models.Model):
    body = models.CharField(max_length=155)
    completed = models.BooleanField(default=False)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body}'

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'ToDo'
        verbose_name = 'ToDo'
