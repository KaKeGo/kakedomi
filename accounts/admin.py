from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
User,
)
from .forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'last_login')
    list_filter = ('username', 'email')
    ordering = ('-date_joined',)
    readonly_fields = ('password',)
    fieldsets = (
        ('Info', {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ['email', 'username']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
