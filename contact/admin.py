from django.contrib import admin

from .models import ContactMessage, Contact

# Register your models here.


admin.site.register([Contact, ContactMessage])
