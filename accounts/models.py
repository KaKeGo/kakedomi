from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    reg = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField('Friend', related_name='my_friends')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} {self.user.id}'

    def get_profile_absolute_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username) + str(self.user.id))
        super(Profile, self).save(*args, **kwargs)

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}'

class RegimentBody(models.Model):
    body = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.body}'

class Regiment(models.Model):
    title = models.CharField(max_length=20, unique=True)
    reg_body = models.ManyToManyField('RegimentBody')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_regiment_absolute_url(self):
        return reverse('accounts:regiment_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(Regiment, self).save(*args, **kwargs)
