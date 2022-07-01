from django.contrib import admin

from .models import (
User,
)

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login')
    list_filter = ('username', 'email')
    ordering = ('-date_joined',)
    readonly_fields = ('password',)
    fieldsets = (
        ('Info', {'fields': ('email', 'username', 'password')}),
        ('Additional', {'fields': ()}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff', 'is_active')}),
    )
